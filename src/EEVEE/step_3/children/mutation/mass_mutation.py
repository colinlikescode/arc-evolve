"""
Mass Mutation phase - runs AFTER all islands complete if no 100% solution found.

Uses context from the top island and runs 5 rounds:
- Round 1: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 1 (0-99)
- Round 2: Gemini 3 Pro (1 call) - regular prompt
- Round 3: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 2 (100-199)
- Round 4: Claude 4.5 Opus (1 call) - regular prompt
- Round 5: Grok 4.1 Fast Reasoning (100 parallel calls) - mass mutation hints set 3 (200-299)
"""
import asyncio
import importlib
from typing import Optional, List
from ..types.island_types import Solution, IslandResult, TrainResult, TestResult
from ..utils.friends import extract_all_solutions, extract_code, extract_instructions, create_solution_examples
from EEVEE.prompts.solver_prompt import build_solver_prompt, _get_step2_formulate
from EEVEE.prompts.feedback_prompt import build_feedback_prompt
from EEVEE.prompts.mass_mutation_prompt import get_mass_mutation_pattern, build_mass_mutation_hint
from ..llm.llm_wrappers import call_grok, call_gemini_pro, call_claude_opus
from ..solvers.single_solver import _run_on_test

# Import verifier module
_verifier_module = importlib.import_module('EEVEE.step_3.children.verifier.evaluator')
evaluate_on_training = _verifier_module.evaluate_on_training


async def run_mass_mutation_phase(
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    island_attempts: list[Solution],
    problem_text: str,
    pattern_hints: str = "",
    problem_id: str = "",
    mutation_id: int = 1,
) -> Optional[IslandResult]:
    """
    Run a full mass mutation phase: 5 rounds.
    
    Round 1: Grok (100 parallel) - mass mutation hints set 1 (0-99)
    Round 2: Gemini (1 call) - regular prompt
    Round 3: Grok (100 parallel) - mass mutation hints set 2 (100-199)
    Round 4: Claude (1 call) - regular prompt
    Round 5: Grok (100 parallel) - mass mutation hints set 3 (200-299)
    
    Args:
        train_in: Training input grids
        train_out: Training output grids
        test_in: Test input grids
        island_attempts: Previous solution attempts from the source island
        problem_text: Formatted problem string
        pattern_hints: Original pattern hints (from visual priors)
        problem_id: Problem ID for logging
        mutation_id: Always 1 (kept for compatibility, but only one mass mutation phase exists)
    
    Returns:
        IslandResult if a 100% solution is found, None otherwise
    """
    special_id = 99  # Special ID for Mass Mutation
    
    print(f"\n{'='*70}")
    print(f"🧬 MASS MUTATION: Starting 5 rounds")
    print(f"{'='*70}")
    print(f"   📚 Top island has {len(island_attempts)} attempts (using top 5 as context)")
    
    # Round pattern: Grok (100), Gemini (1), Grok (100), Claude (1), Grok (100)
    # 100-call rounds use mass mutation hints (no pattern hints)
    # Single-call rounds use pattern hints
    round_configs = [
        {"model": "grok", "count": 100, "use_hints": False},      # Hints set 1 (0-99)
        {"model": "gemini", "count": 1, "use_hints": True},       # Pattern hints
        {"model": "grok", "count": 100, "use_hints": False},      # Hints set 2 (100-199)
        {"model": "claude", "count": 1, "use_hints": True},       # Pattern hints
        {"model": "grok", "count": 100, "use_hints": False},      # Hints set 3 (200-299)
    ]
    
    # Accumulate attempts across rounds
    all_attempts = list(island_attempts)
    best_score = 0.0
    best_result: Optional[IslandResult] = None
    
    total_rounds = len(round_configs)
    for round_num, config in enumerate(round_configs):
        model = config["model"]
        count = config["count"]
        use_hints = config["use_hints"]
        
        model_display = {
            "grok": "GROK (100 parallel)",
            "gemini": "GEMINI (1 call)",
            "claude": "CLAUDE (1 call)",
        }[model]
        
        print(f"\n   🧬 MASS MUTATION ROUND {round_num + 1}/{total_rounds}: {model_display}", flush=True)
        
        if model == "grok":
            result = await _run_grok_round(
                train_in=train_in,
                train_out=train_out,
                test_in=test_in,
                attempts=all_attempts,
                problem_text=problem_text,
                pattern_hints=pattern_hints,
                round_num=round_num,
                problem_id=problem_id,
            )
        elif model == "gemini":
            result = await _run_gemini_round(
                train_in=train_in,
                train_out=train_out,
                test_in=test_in,
                attempts=all_attempts,
                problem_text=problem_text,
                pattern_hints=pattern_hints,
                round_num=round_num,
                problem_id=problem_id,
            )
        else:  # claude
            result = await _run_claude_round(
                train_in=train_in,
                train_out=train_out,
                test_in=test_in,
                attempts=all_attempts,
                problem_text=problem_text,
                pattern_hints=pattern_hints,
                round_num=round_num,
                problem_id=problem_id,
            )
        
        if result is None:
            print(f"   ⚠️ Round {round_num + 1} produced no valid solutions", flush=True)
            continue
        
        solution, score, all_correct, train_res, test_res = result
        
        # Add solution to attempts for next round
        all_attempts.append(solution)
        
        print(f"   🎯 Round {round_num + 1} best: {score:.1%}", flush=True)
        
        # Track best result
        if score > best_score:
            best_score = score
            best_result = IslandResult(
                train_results=train_res,
                results=test_res,
                iteration=round_num + 1,
                island_id=special_id,  # 99 for Mass Mutation
                attempts=all_attempts
            )
        
        # Early exit if perfect solution found
        if all_correct:
            print(f"\n   🎉 MASS MUTATION SUCCESS! Found 100% solution in round {round_num + 1}!", flush=True)
            return IslandResult(
                train_results=train_res,
                results=test_res,
                iteration=round_num + 1,
                island_id=special_id,  # 99 for Mass Mutation
                attempts=all_attempts
            )
    
    print(f"\n   📊 Mass Mutation complete. Best score: {best_score:.1%}")
    return best_result


async def _run_grok_round(
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    attempts: list[Solution],
    problem_text: str,
    pattern_hints: str,
    round_num: int,
    problem_id: str,
) -> Optional[tuple[Solution, float, bool, list[TrainResult], list[TestResult]]]:
    """
    Run a single Grok round: 100 parallel calls with mass mutation hints.
    
    Returns:
        Tuple of (best_solution, score, all_correct, train_results, test_results) or None
    """
    print(f"   📡 Launching 100 Grok calls (batches of 20, 20s apart)...", flush=True)
    
    # Build feedback from previous attempts
    feedback_section = None
    if attempts:
        examples_text = create_solution_examples(
            attempts, max_examples=5, ascending_score_order=True
        )
        feedback_section = build_feedback_prompt(examples_text)
        print(f"   📚 Including {min(5, len(attempts))} previous attempts as context", flush=True)
    
    # Launch 100 tasks in batches of 20, 20 seconds apart
    # All tasks run concurrently once launched
    tasks = []
    for batch_start in range(0, 100, 20):
        batch_end = min(batch_start + 20, 100)
        print(f"   📡 Launching Grok calls {batch_start+1}-{batch_end}...", flush=True)
        
        for i in range(batch_start, batch_end):
            pattern = get_mass_mutation_pattern(i, round_num)
            mass_mutation_hint = build_mass_mutation_hint(pattern)
            
            # Grok uses ONLY mass mutation hints (no pattern hints)
            prompt = build_solver_prompt(problem_text, pattern_hints=mass_mutation_hint)
            
            # Replace STEP 2 with feedback from previous attempts
            if feedback_section:
                step2_formulate = _get_step2_formulate()
                prompt = prompt.replace(step2_formulate, feedback_section)
            
            # Create task
            task = asyncio.create_task(
                call_grok(prompt, context=f"MM Round {round_num+1} Pattern {i+1}")
            )
            tasks.append((i, task))
        
        # Wait 20 seconds before next batch (skip after last batch)
        if batch_end < 100:
            await asyncio.sleep(20)
    
    # Wait for all calls to complete
    print(f"   ⏳ Waiting for 100 Grok calls to complete...", flush=True)
    results = []
    for i, task in tasks:
        try:
            response = await task
            if response:
                results.append((i, response))
        except Exception as e:
            print(f"   ⚠️ Grok call {i+1} failed: {e}", flush=True)
    
    print(f"   ✅ Received {len(results)}/100 responses", flush=True)
    
    # Extract and evaluate all solutions in parallel
    return await _evaluate_responses(results, train_in, train_out, test_in)


async def _run_gemini_round(
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    attempts: list[Solution],
    problem_text: str,
    pattern_hints: str,
    round_num: int,
    problem_id: str,
) -> Optional[tuple[Solution, float, bool, list[TrainResult], list[TestResult]]]:
    """
    Run a single Gemini round: 1 call with regular prompt (no mass mutation hints).
    
    Returns:
        Tuple of (best_solution, score, all_correct, train_results, test_results) or None
    """
    print(f"   📡 Calling Gemini 3 Pro with regular prompt...", flush=True)
    
    # Build feedback from previous attempts
    feedback_section = None
    if attempts:
        examples_text = create_solution_examples(
            attempts, max_examples=5, ascending_score_order=True
        )
        feedback_section = build_feedback_prompt(examples_text)
        print(f"   📚 Including {min(5, len(attempts))} previous attempts as context", flush=True)
    
    # Gemini uses the REGULAR solver prompt WITH pattern hints (no mass mutation hints)
    prompt = build_solver_prompt(problem_text, pattern_hints=pattern_hints)
    
    # Replace STEP 2 with feedback from previous attempts
    if feedback_section:
        step2_formulate = _get_step2_formulate()
        prompt = prompt.replace(step2_formulate, feedback_section)
    
    try:
        response = await call_gemini_pro(prompt, context=f"MM Round {round_num+1} Gemini")
        if response:
            results = [(0, response)]
            return await _evaluate_responses(results, train_in, train_out, test_in)
    except Exception as e:
        print(f"   ⚠️ Gemini call failed: {e}", flush=True)
    
    return None


async def _run_claude_round(
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
    attempts: list[Solution],
    problem_text: str,
    pattern_hints: str,
    round_num: int,
    problem_id: str,
) -> Optional[tuple[Solution, float, bool, list[TrainResult], list[TestResult]]]:
    """
    Run a single Claude round: 1 call with regular prompt (no mass mutation hints).
    
    Returns:
        Tuple of (best_solution, score, all_correct, train_results, test_results) or None
    """
    print(f"   📡 Calling Claude 4.5 Opus with regular prompt...", flush=True)
    
    # Build feedback from previous attempts
    feedback_section = None
    if attempts:
        examples_text = create_solution_examples(
            attempts, max_examples=5, ascending_score_order=True
        )
        feedback_section = build_feedback_prompt(examples_text)
        print(f"   📚 Including {min(5, len(attempts))} previous attempts as context", flush=True)
    
    # Claude uses the REGULAR solver prompt WITH pattern hints (no mass mutation hints)
    prompt = build_solver_prompt(problem_text, pattern_hints=pattern_hints)
    
    # Replace STEP 2 with feedback from previous attempts
    if feedback_section:
        step2_formulate = _get_step2_formulate()
        prompt = prompt.replace(step2_formulate, feedback_section)
    
    try:
        response = await call_claude_opus(prompt, context=f"MM Round {round_num+1} Claude")
        if response:
            results = [(0, response)]
            return await _evaluate_responses(results, train_in, train_out, test_in)
    except Exception as e:
        print(f"   ⚠️ Claude call failed: {e}", flush=True)
    
    return None


async def _evaluate_responses(
    results: list[tuple[int, str]],
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    test_in: list[list[list[int]]],
) -> Optional[tuple[Solution, float, bool, list[TrainResult], list[TestResult]]]:
    """
    Extract and evaluate solutions from LLM responses in parallel.
    
    Returns:
        Tuple of (best_solution, score, all_correct, train_results, test_results) or None
    """
    # First, extract all solutions from all responses
    all_candidates = []
    for i, response in results:
        solutions = extract_all_solutions(response)
        if not solutions:
            # Fallback to single extraction
            code = extract_code(response)
            if code:
                solutions = [(extract_instructions(response), code)]
        
        for instructions, code in solutions:
            if code:
                all_candidates.append((i, instructions, code))
    
    if not all_candidates:
        return None
    
    print(f"   🔍 Evaluating {len(all_candidates)} solutions in parallel...", flush=True)
    
    # Parallelize evaluation of all solutions
    async def evaluate_single_solution(pattern_idx: int, instructions: str, code: str):
        """Evaluate a single solution on training examples."""
        try:
            # Run synchronous evaluate_on_training in thread pool
            train_results, score, all_correct = await asyncio.to_thread(
                evaluate_on_training, code, train_in, train_out
            )
            return {
                "code": code,
                "explanation": instructions,
                "feedback": "",
                "score": score,
                "pattern_index": pattern_idx,
                "all_correct": all_correct,
                "train_results": train_results,
            }
        except Exception as e:
            return None
    
    # Create tasks for all solutions
    tasks = [
        evaluate_single_solution(pattern_idx, instructions, code)
        for pattern_idx, instructions, code in all_candidates
    ]
    
    # Wait for all evaluations to complete
    evaluated_solutions = await asyncio.gather(*tasks)
    
    # Filter out None results (failed evaluations)
    all_solutions = [s for s in evaluated_solutions if s is not None]
    
    if not all_solutions:
        return None
    
    # Sort by score and get best
    all_solutions.sort(key=lambda x: x["score"], reverse=True)
    best = all_solutions[0]
    
    print(f"   ✅ Evaluated {len(all_solutions)}/{len(all_candidates)} solutions successfully", flush=True)
    print(f"   🎯 Best solution score: {best['score']:.5%} (all_correct: {best['all_correct']})", flush=True)
    
    # Execute best on test inputs
    test_results = _run_on_test(best["code"], test_in, timeout_s=5.0)
    
    solution = Solution(
        code=best["code"],
        explanation=best["explanation"],
        feedback="",
        score=best["score"]
    )
    
    return (solution, best["score"], best["all_correct"], best["train_results"], test_results)
