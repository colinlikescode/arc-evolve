"""
Single island solver.

Runs one island through evolution iterations,
using probabilistic selection of previous solutions for feedback.
"""
import asyncio
import importlib
import json
import re
from typing import Any, Optional, List, Dict
import numpy as np

from ..types.island_types import IslandResult, Solution, TrainResult, TestResult, IslandConfig
from ..utils.executor import run_code, execute_on_single_input_sync
from ..utils.friends import (
    extract_code as _extract_code,
    extract_instructions as _extract_instructions,
    extract_all_solutions as _extract_all_solutions,
    create_solution_examples as _create_solution_examples,
)
from EEVEE.prompts.solver_prompt import build_solver_prompt, _get_step2_formulate
from EEVEE.prompts.feedback_prompt import build_feedback_prompt

# Import verifier module
_verifier_module = importlib.import_module('EEVEE.step_3.children.verifier.evaluator')
evaluate_on_training = _verifier_module.evaluate_on_training
build_feedback_from_results = _verifier_module.build_feedback_from_results


async def run_single_island(
    *,
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    config: IslandConfig,
    llm_call_func,
    pattern_hints: str = "",
    problem_id: str | None = None,
    island_id: int = 0,
    llm_call_func_switched = None,
    llm_call_func_claude = None,
) -> IslandResult:
    """
    Run a single island through full evolution.
    
    Args:
        train_in: List of training input grids
        train_out: List of training output grids
        test_in: List of test input grids
        config: Island configuration
        llm_call_func: Async function to call LLM
        pattern_hints: Visual prior hints
        problem_id: Problem ID for logging
        island_id: Which island (0-4) this is
        llm_call_func_switched: Optional LLM function to switch to after N iterations
    
    Returns:
        IslandResult with train_results, results (test), iteration, and island_id
    """
    max_iterations = int(config["max_iterations"])
    max_feedback_examples = int(config.get("max_feedback_examples", 5))
    feedback_selection_rate = float(config.get("feedback_selection_rate", 1.0))
    seed = int(config.get("seed", 0))
    randomize_training_order = bool(config.get("randomize_training_order", True))
    ascending_score_order = bool(config.get("ascending_score_order", True))
    return_best = bool(config.get("return_best_result", True))
    timeout_s = float(config.get("timeout_s", 5.0))
    per_iteration_retries = int(config.get("per_iteration_retries", 2))
    
    switch_after = config.get("switch_llm_after", None)
    switch_to_llm_id = config.get("switch_to_llm_id", None)
    claude_rounds = config.get("claude_rounds", [])
    expert_id = config.get("llm_id", "unknown")
    
    # Build island name for logging
    island_name = _build_island_name(
        island_id, expert_id, seed, max_iterations, claude_rounds,
        switch_after, switch_to_llm_id, problem_id
    )
    
    highest_score_seen = -1.0
    best_result_so_far: Optional[IslandResult] = None
    final_train: list[TrainResult] = [
        TrainResult(success=False, output="", soft_score=0.0, error="No solutions generated", code="")
    ]
    final_test: Optional[list[TestResult]] = None
    
    random_generator = np.random.default_rng(seed)
    previous_attempts: list[Solution] = []
    
    for iteration_num in range(max_iterations):
        example_dict = _prepare_example(train_in, train_out, test_in)
        problem_text = _format_problem(example_dict, randomize_training_order, seed + iteration_num)
        prompt = build_solver_prompt(problem_text, pattern_hints)
        
        # Select previous solutions probabilistically for feedback
        chosen = []
        if previous_attempts:
            num_attempts = len(previous_attempts)
            random_values = random_generator.uniform(size=num_attempts)
            selection_mask = random_values < feedback_selection_rate
            chosen = [attempt for attempt, should_select in zip(previous_attempts, selection_mask, strict=False) if should_select]
            print(f"   📚 {island_name}: Selected {len(chosen)}/{len(previous_attempts)} previous solutions for feedback", flush=True)
        
        if chosen:
            examples_text = _create_solution_examples(
                chosen, max_examples=max_feedback_examples, ascending_score_order=ascending_score_order
            )
            scores = [s.get("score", 0.0) if isinstance(s, dict) else getattr(s, "score", 0.0) for s in chosen]
            if scores:
                print(f"   📚 {island_name}: Feedback scores range: {min(scores):.1%} - {max(scores):.1%}", flush=True)
            feedback_section = build_feedback_prompt(examples_text)
            step2_formulate = _get_step2_formulate()
            prompt = prompt.replace(step2_formulate, feedback_section)
        
        # Determine which LLM to use for this iteration
        is_claude_round = iteration_num in claude_rounds
        
        if is_claude_round:
            if llm_call_func_claude is None:
                print(f"   ⚠️ {island_name}: Claude rounds specified but no Claude function provided", flush=True)
                current_llm_func = llm_call_func
            else:
                current_llm_func = llm_call_func_claude
                print(f"   🔄 {island_name}: Using Claude for iteration {iteration_num + 1}", flush=True)
        elif switch_after is not None and iteration_num >= switch_after and llm_call_func_switched is not None:
            current_llm_func = llm_call_func_switched
            if iteration_num == switch_after:
                print(f"   🔄 {island_name}: Switching to {switch_to_llm_id.upper()}", flush=True)
        else:
            current_llm_func = llm_call_func
        
        # Call LLM with retry logic
        response = None
        for retry_attempt in range(per_iteration_retries + 1):
            try:
                response = await current_llm_func(
                    prompt, context=f"Iteration {iteration_num + 1} [{problem_id or ''}]"
                )
                if response:
                    break
            except Exception as e:
                if retry_attempt < per_iteration_retries:
                    print(f"   ⚠️ {island_name}: LLM call failed, retrying... {str(e)[:80]}", flush=True)
                else:
                    print(f"   ⚠️ {island_name}: LLM call failed after retries: {e}", flush=True)
            
            if not response and retry_attempt < per_iteration_retries:
                backoff = 2 ** retry_attempt
                await asyncio.sleep(backoff)
        
        if not response:
            continue
        
        # Extract solutions from response
        all_solutions = _extract_all_solutions(response)
        if not all_solutions:
            code = _extract_code(response)
            if code:
                all_solutions = [(_extract_instructions(response), code)]
        
        if not all_solutions:
            print(f"   ⚠️ {island_name}: Failed to extract code in iteration {iteration_num + 1}", flush=True)
            continue
        
        print(f"   ✅ {island_name}: Extracted {len(all_solutions)} solution(s)", flush=True)
        
        # Evaluate all solutions and pick the best
        best_score = -1
        best_idx = 0
        code = None
        instructions = ""
        train_res = []
        score = 0.0
        all_correct = False
        
        for idx, (instr, candidate_code) in enumerate(all_solutions):
            try:
                cand_train_res, cand_score, cand_all_correct = evaluate_on_training(
                    candidate_code, train_in, train_out
                )
                num_correct = sum(1 for r in cand_train_res if r.get("success", False))
                print(f"      Sol {idx+1}: {num_correct}/{len(cand_train_res)} correct ({cand_score:.1%})", flush=True)
                
                if cand_score > best_score:
                    best_score = cand_score
                    best_idx = idx
                    code = candidate_code
                    instructions = instr
                    train_res = cand_train_res
                    score = cand_score
                    all_correct = cand_all_correct
            except Exception as e:
                print(f"      Sol {idx+1}: ❌ failed ({str(e)[:50]})", flush=True)
        
        if code is None:
            print(f"   ❌ {island_name}: All solutions failed evaluation", flush=True)
            continue
        
        if len(all_solutions) > 1:
            print(f"      → Best: Sol {best_idx+1} ({score:.1%})", flush=True)
        
        solution = Solution(code=code, explanation=instructions, feedback="", score=score)
        previous_attempts.append(solution)
        
        test_res = _run_on_test(code, test_in, timeout_s=timeout_s)
        final_train, final_test = train_res, test_res
        
        # Perfect solution found - return immediately
        if all_correct:
            previous_attempts.append(Solution(code=code, explanation=instructions, feedback="PERFECT", score=1.0))
            print(f"\n   🎉 {island_name} got ALL TRAINING EXAMPLES CORRECT in iteration {iteration_num + 1}!", flush=True)
            return IslandResult(
                train_results=train_res, results=test_res, iteration=iteration_num + 1, island_id=island_id,
                attempts=previous_attempts
            )
        
        feedback = build_feedback_from_results(train_res, train_out)
        previous_attempts.append(Solution(code=code, explanation=instructions, feedback=feedback, score=score))
        
        # Track best result
        if highest_score_seen < score or highest_score_seen < 0:
            improvement = score - highest_score_seen if highest_score_seen >= 0 else score
            highest_score_seen = score
            print(f"      📈 +{improvement:.1%}", flush=True)
            best_result_so_far = IslandResult(
                train_results=train_res, results=test_res, iteration=iteration_num + 1, island_id=island_id,
                attempts=list(previous_attempts)
            )
    
    # Return best or final result
    if return_best and best_result_so_far is not None:
        best_result_so_far["attempts"] = previous_attempts
        return best_result_so_far
    
    if final_test is None:
        final_test = [TestResult(success=False, output="", soft_score=0.0, error="No valid solutions", code="")]
    
    return IslandResult(
        train_results=final_train, results=final_test, iteration=max_iterations, island_id=island_id,
        attempts=previous_attempts
    )


def _build_island_name(
    island_id: int, expert_id: str, seed: int, max_iterations: int,
    claude_rounds: list, switch_after: Optional[int], switch_to_llm_id: Optional[str],
    problem_id: Optional[str]
) -> str:
    """Build descriptive island name for logging."""
    if claude_rounds:
        claude_sorted = sorted(claude_rounds)
        max_iter = max_iterations - 1
        claude_start, claude_end = claude_sorted[0], claude_sorted[-1]
        
        parts = []
        if claude_start == 0:
            parts.append(f"Claude(r{claude_start+1}-{claude_end+1})")
            if claude_end < max_iter:
                parts.append(f"{expert_id.upper()}(r{claude_end+2}-{max_iter+1})")
        elif claude_end == max_iter:
            if claude_start > 0:
                parts.append(f"{expert_id.upper()}(r1-{claude_start})")
            parts.append(f"Claude(r{claude_start+1}-{claude_end+1})")
        else:
            if claude_start > 0:
                parts.append(f"{expert_id.upper()}(r1-{claude_start})")
            parts.append(f"Claude(r{claude_start+1}-{claude_end+1})")
            if claude_end < max_iter:
                parts.append(f"{expert_id.upper()}(r{claude_end+2}-{max_iter+1})")
        
        model_desc = "→".join(parts)
    elif switch_after is not None and switch_to_llm_id is not None:
        model_desc = f"{expert_id.upper()}→{switch_to_llm_id.upper()}"
    else:
        model_desc = expert_id.upper()
    
    base = f"Island {island_id + 1} ({model_desc}, seed={seed})"
    return f"{base} [Q{problem_id}]" if problem_id else base


def _prepare_example(train_in, train_out, test_in) -> dict[str, Any]:
    """Prepare example dictionary."""
    train = [{"input": inp, "output": out} for inp, out in zip(train_in, train_out, strict=True)]
    test = [{"input": inp} for inp in test_in]
    return {"train": train, "test": test}


def _format_problem(problem: dict[str, Any], randomize_order: bool = False, seed: Optional[int] = None) -> str:
    """Format problem as text with optional randomization."""
    training_examples = list(problem["train"])
    test_inputs = list(problem["test"])
    
    if randomize_order and len(training_examples) > 1:
        generator = np.random.default_rng(seed or 0)
        shuffled_indices = generator.permutation(len(training_examples))
        training_examples = [training_examples[idx] for idx in shuffled_indices]
    
    examples_text = ""
    for idx, example in enumerate(training_examples, start=1):
        input_grid = _grid_to_diagram(example["input"])
        output_grid = _grid_to_diagram(example["output"])
        examples_text += f"\nExample #{idx}\nInput:\n<Diagram>\n{input_grid}\n</Diagram>\n\nOutput:\n<Diagram>\n{output_grid}\n</Diagram>\n"
    
    challenges_text = ""
    for idx, challenge in enumerate(test_inputs, start=1):
        input_grid = _grid_to_diagram(challenge["input"])
        challenges_text += f"\nChallenge #{idx}\nInput:\n<Diagram>\n{input_grid}\n</Diagram>\n"
    
    return examples_text + challenges_text


def _grid_to_diagram(grid: list[list[int]] | np.ndarray) -> str:
    """Convert grid to ASCII diagram."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def _run_on_test(code: str, test_in: list[list[list[int]]], *, timeout_s: float = 5.0) -> list[TestResult]:
    """Execute code on test inputs."""
    execute_code_on_input = _verifier_module.execute_code_on_input
    
    test_results: list[TestResult] = []
    for inp in test_in:
        output_grid = execute_code_on_input(code, inp)
        
        if output_grid is None:
            test_results.append(TestResult(success=False, output="", soft_score=0.0, error="Execution failed", code=code))
        else:
            out_str = json.dumps(output_grid)
            test_results.append(TestResult(success=False, output=out_str, soft_score=0.0, error=None, code=code))
    
    return test_results
