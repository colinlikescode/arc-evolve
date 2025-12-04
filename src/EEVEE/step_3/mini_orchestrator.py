"""
Step 3 Mini Orchestrator: Run parallel Python islands with voting.

This is the main entry point for Step 3.
If no island achieves 100%, triggers mass mutation phase with Grok.
"""
from typing import Dict, Any
import copy

from .config import EXPERT_CONFIGS
from .children.solvers.parallel_solver import run_parallel_islands, _vote_on_results
from .children.mutation.mass_mutation import run_mass_mutation_phase
from .children.llm.llm_wrappers import call_claude_opus, call_gemini_pro
from .children.solvers.single_solver import _prepare_example, _format_problem


def _compute_output_signature(test_outputs):
    """Compute signature from test results (for grouping identical outputs)."""
    signature_parts = []
    for output_entry in test_outputs:
        output_value = output_entry.get("output", "")
        signature_parts.append(output_value)
    return str(signature_parts)


def _execute_code_on_test_inputs(code: str, test_in: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Execute code on all test inputs and return actual output grids.
    
    Args:
        code: Python code to execute
        test_in: List of test input grids
    
    Returns:
        List of output grids (same length as test_in, None for failed executions)
    """
    # Use absolute import to avoid Python 3.x issues with numeric module names
    import importlib
    verifier_module = importlib.import_module('EEVEE.step_3.children.verifier.evaluator')
    execute_code_on_input = verifier_module.execute_code_on_input
    
    outputs = []
    for inp in test_in:
        output_grid = execute_code_on_input(code, inp)
        outputs.append(output_grid)  # Can be None if execution failed
    
    return outputs


def _outputs_are_different(outputs1: list[list[list[int]]], outputs2: list[list[list[int]]]) -> bool:
    """
    Compare two output lists to see if they're different.
    
    Args:
        outputs1: First list of output grids (can contain None for failed executions)
        outputs2: Second list of output grids (can contain None for failed executions)
    
    Returns:
        True if outputs are different, False if identical
    """
    if len(outputs1) != len(outputs2):
        return True
    
    for out1, out2 in zip(outputs1, outputs2):
        # If either is None (execution failed), consider them different
        if out1 is None or out2 is None:
            if out1 != out2:
                return True
            continue
        
        # Compare grids element by element
        if out1 != out2:
            return True
    
    return False


def _get_llm_function(llm_id: str):
    """
    Map llm_id to the corresponding LLM call function.
    
    Args:
        llm_id: "claude", "gemini", or "grok"
    
    Returns:
        Async function to call the LLM
    """
    if llm_id == "claude":
        return call_claude_opus
    elif llm_id == "gemini":
        return call_gemini_pro
    elif llm_id == "grok":
        from .children.llm.llm_wrappers import call_grok
        return call_grok
    else:
        raise ValueError(f"Unknown llm_id: {llm_id}. Must be 'claude', 'gemini', or 'grok'")


def _get_model_name(llm_id: str) -> str:
    """Get human-readable model name for logging."""
    if llm_id == "claude":
        return "Claude Opus 4.5"
    elif llm_id == "gemini":
        return "Gemini 3 Pro"
    elif llm_id == "grok":
        return "Grok 4.1 Fast Reasoning"
    else:
        return f"Unknown ({llm_id})"


async def execute_step_3(question_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute Step 3: Run parallel Python islands with voting.
    
    Number of islands and models are configured in config.py via EXPERT_CONFIGS.
    
    Args:
        question_data: Contains train_examples, test_inputs, pattern_detector_hints_python, etc.
    
    Returns:
        Dict with ordered results (voted), top result data, etc.
    """
    # Extract inputs
    train_examples = question_data.get("train_examples", question_data.get("training_examples", []))
    test_inputs = question_data.get("test_inputs", [])
    pattern_hints = question_data.get("pattern_detector_hints_python", "")
    question_id = question_data.get("question_id", "unknown")
    
    # Convert to format solver expects
    train_in = [ex["input"] for ex in train_examples]
    train_out = [ex["output"] for ex in train_examples]
    test_in = test_inputs  # Already list of grids
    
    # Prepare island configs (copy to avoid mutation)
    configs = [copy.deepcopy(island_config) for island_config in EXPERT_CONFIGS]
    
    # Build LLM call functions based on config
    llm_funcs = []
    llm_funcs_switched = []
    llm_funcs_claude = []
    for island_config in configs:
        llm_id = island_config.get("llm_id", "unknown")
        llm_funcs.append(_get_llm_function(llm_id))
        
        # Check if this is a hybrid island that switches LLMs
        switch_to_llm_id = island_config.get("switch_to_llm_id", None)
        if switch_to_llm_id:
            llm_funcs_switched.append(_get_llm_function(switch_to_llm_id))
        else:
            llm_funcs_switched.append(None)
        
        # Check if island uses Claude in specific rounds (Grok only used in mass mutation phase)
        claude_rounds = island_config.get("claude_rounds", [])
        if claude_rounds:
            llm_funcs_claude.append(_get_llm_function("claude"))
        else:
            llm_funcs_claude.append(None)
    
    # Count islands by model (including hybrid islands)
    claude_count = sum(1 for island_config in configs if island_config.get("llm_id") == "claude" or island_config.get("switch_to_llm_id") == "claude")
    gemini_count = sum(1 for island_config in configs if island_config.get("llm_id") == "gemini" or island_config.get("switch_to_llm_id") == "gemini")
    grok_count = sum(1 for island_config in configs if island_config.get("llm_id") == "grok" or island_config.get("switch_to_llm_id") == "grok")
    
    print(f"\n{'='*70}")
    print(f"🔀 STEP 3: Parallel Python Islands ({len(configs)} total)")
    print(f"{'='*70}")
    print(f"   🐍 Running {len(configs)} islands in parallel...")
    for i, island_config in enumerate(configs, 1):
        llm_id = island_config.get("llm_id", "unknown")
        switch_to = island_config.get("switch_to_llm_id", None)
        switch_after = island_config.get("switch_llm_after", None)
        
        if switch_to and switch_after:
            model_name = f"{_get_model_name(llm_id)} → {_get_model_name(switch_to)} (after {switch_after} rounds)"
        else:
            model_name = _get_model_name(llm_id)
        print(f"      • Island {i}: {model_name} (seed={island_config.get('seed', 0)})")
    if claude_count > 0:
        print(f"   📊 {claude_count} Claude island(s)")
    if gemini_count > 0:
        print(f"   📊 {gemini_count} Gemini island(s)")
    if grok_count > 0:
        print(f"   📊 {grok_count} Grok island(s)")
    
    # Run parallel islands with voting
    ranked_results = await run_parallel_islands(
        train_in=train_in,
        train_out=train_out,
        test_in=test_in,
        island_configs=configs,
        llm_call_funcs=llm_funcs,
        llm_call_funcs_switched=llm_funcs_switched,
        llm_call_funcs_claude=llm_funcs_claude,
        pattern_hints=pattern_hints,
        problem_id=str(question_id),
    )
    
    # Get top result and check if any island got 100%
    top_result = ranked_results[0] if ranked_results else None
    any_perfect = False
    if top_result:
        train_results_check = top_result.get("train_results", [])
        any_perfect = all(run_result.get("success", False) for run_result in train_results_check)
    
    # If no 100% answer, run mass mutation FIRST, then do voting
    if not any_perfect and top_result:
        # Format problem text for mass mutation
        example_dict = _prepare_example(train_in, train_out, test_in)
        problem_text = _format_problem(example_dict, randomize_order=False, seed=0)
        
        # ========== MASS MUTATION: Using HIGHEST SCORING island context ==========
        # Find the island with the highest score (not just most votes)
        highest_scoring_island = top_result
        highest_score = 0.0
        for result in ranked_results:
            train_res = result.get("train_results", [])
            if train_res:
                scores = [r.get("soft_score", 0.0) for r in train_res]
                mean_score = sum(scores) / len(scores) if scores else 0.0
                if mean_score > highest_score:
                    highest_score = mean_score
                    highest_scoring_island = result
        
        print(f"\n   ⚠️ No island achieved 100%. Triggering Mass Mutation (highest scoring island: {highest_score:.1%})...")
        
        # Get attempts from the highest scoring island
        top_island_attempts = highest_scoring_island.get("attempts", [])
        
        # Run mass mutation phase
        mutation_result = await run_mass_mutation_phase(
            train_in=train_in,
            train_out=train_out,
            test_in=test_in,
            island_attempts=top_island_attempts,
            problem_text=problem_text,
            pattern_hints=pattern_hints,
            problem_id=str(question_id),
            mutation_id=1,
        )
        
        # Check if Mass Mutation found a perfect result
        mutation_perfect = False
        if mutation_result:
            m_train_results = mutation_result.get("train_results", [])
            mutation_perfect = all(run_result.get("success", False) for run_result in m_train_results)
            m_scores = [run_result.get("soft_score", 0.0) for run_result in m_train_results]
            m_mean_score = sum(m_scores) / len(m_scores) if m_scores else 0.0
            
            # Check if Mass Mutation result is better than top result
            top_scores = [run_result.get("soft_score", 0.0) for run_result in top_result.get("train_results", [])]
            top_mean_score = sum(top_scores) / len(top_scores) if top_scores else 0.0
            
            if mutation_perfect or m_mean_score > top_mean_score:
                print(f"   🎯 Mass Mutation found better result: {m_mean_score:.1%} vs {top_mean_score:.1%}")
                ranked_results.insert(0, mutation_result)
                top_result = mutation_result
                any_perfect = mutation_perfect
            else:
                # Mass mutation didn't improve, but add it to ranked results and re-rank using voting logic
                ranked_results.append(mutation_result)
                ranked_results = _vote_on_results(ranked_results)
    
    # Now display voting results (after mass mutation if it ran)
    print(f"\n{'='*70}")
    print(f"🗳️  VOTING RESULTS")
    print(f"{'='*70}")
    
    for i, solver_result in enumerate(ranked_results[:4], 1):  # Show top 4
        iteration = solver_result.get("iteration", 0)
        train_results = solver_result.get("train_results", [])
        all_correct = all(run_result.get("success", False) for run_result in train_results)
        
        # Calculate score
        scores = [run_result.get("soft_score", 0.0) for run_result in train_results]
        mean_score = sum(scores) / len(scores) if scores else 0.0
        
        # Check if this is mass mutation result
        island_id = solver_result.get("island_id", -1)
        if island_id == 99:
            source = "Mass Mutation"
        else:
            # Convert 0-indexed island_id to 1-indexed display (Island 1-5)
            source = f"Island {island_id + 1}"
        
        status = "✅" if all_correct else "❌"
        print(f"   {i}. {status} {source} - Iteration {iteration}: {mean_score:.1%} (all correct: {all_correct})")
    
    # Get top result and second distinct result (if different)
    top_result = ranked_results[0] if ranked_results else None
    chosen_island_id = top_result.get("island_id", -1) if top_result else -1
    
    # Extract test outputs from top result by executing code fresh
    python_answers = []
    python_answers_2 = []
    all_train_correct = False
    top_outputs = None
    
    if top_result:
        train_results = top_result.get("train_results", [])
        all_train_correct = all(run_result.get("success", False) for run_result in train_results)
        
        # Extract code from top result and execute on test inputs
        top_code = None
        if train_results:
            top_code = train_results[0].get("code", "")
        
        if top_code:
            print(f"   🔍 Executing top program on test inputs to get actual outputs...", flush=True)
            top_outputs = _execute_code_on_test_inputs(top_code, test_in)
            # Convert outputs to python_answers format (skip None/failed executions)
            for output_grid in top_outputs:
                if output_grid is not None:
                    python_answers.append(output_grid)
        
        scores = [run_result.get("soft_score", 0.0) for run_result in train_results]
        mean_score = sum(scores) / len(scores) if scores else 0.0
        
        print(f"\n   📊 Top Result: {mean_score:.1%}, {'✅ PERFECT' if all_train_correct else '❌ IMPERFECT'}")
        if chosen_island_id == 99:
            print(f"   🔥 Chosen: MASS MUTATION (top island context)")
        else:
            # Convert 0-indexed island_id to 1-indexed display (Island 1-5)
            print(f"   🏝️  Chosen Island: {chosen_island_id + 1} (of {len(configs)})")
        print(f"   📊 Test outputs generated: {len(python_answers)}")
    
    # Find second distinct solution by executing code and comparing actual outputs
    second_result = None
    second_outputs = None
    
    if top_result and top_outputs is not None and len(ranked_results) > 1:
        print(f"   🔍 Searching for second program with different outputs...", flush=True)
        for idx, solver_result in enumerate(ranked_results[1:], start=2):
            # Extract code from this result
            candidate_train_results = solver_result.get("train_results", [])
            if not candidate_train_results:
                continue
            
            candidate_code = candidate_train_results[0].get("code", "")
            if not candidate_code:
                continue
            
            # Execute code on test inputs
            candidate_outputs = _execute_code_on_test_inputs(candidate_code, test_in)
            
            # Compare with top outputs
            if _outputs_are_different(top_outputs, candidate_outputs):
                second_result = solver_result
                second_outputs = candidate_outputs
                second_island_id = solver_result.get("island_id", -1)
                
                # Convert outputs to python_answers_2 format
                for output_grid in second_outputs:
                    if output_grid is not None:
                        python_answers_2.append(output_grid)
                
                if second_island_id == 99:
                    print(f"   ✅ Found distinct solution from MASS MUTATION (ranked #{idx})")
                else:
                    # Convert 0-indexed island_id to 1-indexed display (Island 1-5)
                    print(f"   ✅ Found distinct solution from Island {second_island_id + 1} (ranked #{idx})")
                break
        
        if not second_result:
            print(f"   ⚠️  No distinct second solution found after checking {len(ranked_results) - 1} candidates")
    
    # If we still don't have a second answer, Step 4 will trigger SUDDEN DEATH
    # to produce an alternative answer. We pass a copy here so Step 4 can detect
    # that both answers are identical and trigger sudden death.
    if python_answers and not python_answers_2:
        print(f"   ⚠️  All programs produce identical outputs. Step 4 will trigger SUDDEN DEATH.")
        python_answers_2 = python_answers.copy()
    
    return {
        **question_data,
        "ordered_results": ranked_results,
        "top_result": top_result,
        "python_answers": python_answers,
        "python_answers_2": python_answers_2 if python_answers_2 else None,
        "python_has_answer": len(python_answers) > 0,
        "python_has_winner": all_train_correct if top_result else False,
        "chosen_island_id": chosen_island_id,
    }

