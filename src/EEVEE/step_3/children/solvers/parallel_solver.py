"""
Parallel solver with voting.

Runs multiple islands in parallel and uses voting to rank results.
"""
import asyncio
import numpy as np
from typing import List, Dict, Any

from ..types.island_types import IslandResult, IslandConfig
from .single_solver import run_single_island


async def run_parallel_islands(
    *,
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    island_configs: list[IslandConfig],
    llm_call_funcs: list,
    llm_call_funcs_switched: list = None,
    llm_call_funcs_claude: list = None,
    pattern_hints: str = "",
    problem_id: str | None = None,
) -> list[IslandResult]:
    """
    Run multiple islands in parallel, then vote on results.
    
    Args:
        train_in: Training input grids
        train_out: Training output grids
        test_in: Test input grids
        island_configs: List of island configurations
        llm_call_funcs: List of LLM call functions (one per island)
        llm_call_funcs_switched: List of switched LLM functions (for hybrid islands)
        pattern_hints: Visual prior hints
        problem_id: Problem ID for logging
    
    Returns:
        Ordered list of results (best first, by voting)
    """
    for island_idx, island_config in enumerate(island_configs):
        iteration_count = island_config["max_iterations"]
        seed_offset = island_idx * iteration_count
        island_config["seed"] = island_config["seed"] + seed_offset
    
    # Default switched funcs to None list
    if llm_call_funcs_switched is None:
        llm_call_funcs_switched = [None] * len(llm_call_funcs)
    if llm_call_funcs_claude is None:
        llm_call_funcs_claude = [None] * len(llm_call_funcs)
    
    # Run islands in parallel
    # All 5 islands receive visual prior hints
    # Pokemon region names for fun logging
    REGION_NAMES = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unova"]
    
    print(f"   📡 Creating {len(island_configs)} island tasks...", flush=True)
    async_tasks = []
    for i, (island_config, llm_func, switched_func, claude_func) in enumerate(zip(island_configs, llm_call_funcs, llm_call_funcs_switched, llm_call_funcs_claude), 1):
        island_idx = i - 1  # 0-indexed
        
        # Check if this island should receive hints (default True for backwards compatibility)
        receives_hints = island_config.get("receives_hints", True)
        island_hints = pattern_hints if receives_hints else ""
        
        # Get Pokemon region name for this island
        region_name = REGION_NAMES[island_idx] if island_idx < len(REGION_NAMES) else f"Island {i}"
        
        # Display island name with hybrid indicator if applicable
        if island_config.get("switch_llm_after") is not None:
            island_name = f"{region_name} ({island_config['llm_id'].upper()}→{island_config.get('switch_to_llm_id', '?').upper()})"
        else:
            island_name = f"{region_name} ({island_config['llm_id'].upper()})"
        
        # Show hint status based on config
        if not receives_hints:
            hint_status = " [NO hints - control]"
        elif island_hints:
            hint_status = " [with hints]"
        else:
            hint_status = ""
        print(f"   📡 Starting {island_name}{hint_status}...", flush=True)
        async_task = asyncio.create_task(
            run_single_island(
                train_in=train_in,
                train_out=train_out,
                test_in=test_in,
                config=island_config,
                llm_call_func=llm_func,
                llm_call_func_switched=switched_func,
                llm_call_func_claude=claude_func,
                pattern_hints=island_hints,
                problem_id=problem_id,
                island_id=island_idx,
            )
        )
        async_tasks.append(async_task)
    
    print(f"   ⏳ Waiting for {len(async_tasks)} islands to complete...", flush=True)
    island_outputs: list[IslandResult] = await asyncio.gather(*async_tasks)
    print(f"   ✅ All {len(island_outputs)} islands completed", flush=True)
    
    ranked_list = _vote_on_results(island_outputs)
    
    return ranked_list


def _vote_on_results(island_outputs: list[IslandResult]) -> list[IslandResult]:
    """
    Vote on results using diversity-first ranking.
    
    Groups results by identical test outputs, then ranks:
    1. Perfect solutions (all training correct) by vote count (descending)
    2. Partial solutions by vote count + soft_score (descending)
    
    Returns ordered list (best first).
    """
    successful_outputs: Dict[str, List[IslandResult]] = {}
    imperfect_outputs: Dict[str, List[IslandResult]] = {}
    
    for solver_result in island_outputs:
        train_results = solver_result.get("train_results", [])
        all_training_correct = all(run_result.get("success", False) for run_result in train_results)
        output_signature = _compute_output_signature(solver_result.get("results", []))
        
        if all_training_correct:
            if output_signature not in successful_outputs:
                successful_outputs[output_signature] = []
            successful_outputs[output_signature].append(solver_result)
        else:
            if output_signature not in imperfect_outputs:
                imperfect_outputs[output_signature] = []
            imperfect_outputs[output_signature].append(solver_result)
    
    successful_clusters: list[list[IslandResult]] = list(successful_outputs.values())
    
    def get_cluster_size(cluster):
        return len(cluster)
    successful_clusters.sort(key=get_cluster_size, reverse=True)
    
    ranked_list: list[IslandResult] = []
    for cluster in successful_clusters:
        if cluster:
            ranked_list.append(cluster[0])
    
    for partial_cluster in imperfect_outputs.values():
        partial_cluster.sort(key=_compute_mean_soft_score, reverse=True)
    
    imperfect_clusters: list[list[IslandResult]] = list(imperfect_outputs.values())
    
    def cluster_sort_key(cluster):
        vote_count = len(cluster)
        best_score = _compute_mean_soft_score(cluster[0]) if cluster else 0.0
        return (vote_count, best_score)
    imperfect_clusters.sort(key=cluster_sort_key, reverse=True)
    
    for cluster in imperfect_clusters:
        if cluster:
            ranked_list.append(cluster[0])
    
    for cluster in successful_clusters:
        ranked_list.extend(cluster[1:])
    
    for cluster in imperfect_clusters:
        ranked_list.extend(cluster[1:])
    
    return ranked_list


def _compute_output_signature(test_outputs: list[Dict[str, Any]]) -> str:
    """Compute signature from test results (for grouping identical outputs)."""
    signature_parts = []
    for output_entry in test_outputs:
        output_value = output_entry.get("output", "")
        signature_parts.append(output_value)
    return str(signature_parts)


def _compute_mean_soft_score(island_result: IslandResult) -> float:
    """Compute mean soft score from train_results."""
    training_results = island_result.get("train_results", [])
    if not training_results:
        return 0.0
    score_values = [run_result.get("soft_score", 0.0) for run_result in training_results]
    return float(np.mean(score_values))

