"""
Step 4 Mini Orchestrator: Format answers for submission.

Uses top solution for Attempt 1, and second distinct solution for Attempt 2 (if available).
If both attempts are identical, triggers SUDDEN DEATH to produce a different answer directly.
Supports questions with multiple test inputs.
"""
import importlib
import json
import re
import asyncio
from typing import Dict, Any, List, Optional

# Use importlib for modules with numeric prefixes (step_4, step_3)
_formatter_module = importlib.import_module('EEVEE.step_4.children.formatter')
_llm_module = importlib.import_module('EEVEE.step_3.children.llm.llm_wrappers')

format_answers = _formatter_module.format_answers
call_gemini_pro = _llm_module.call_gemini_pro

from EEVEE.prompts.sudden_death_prompt import build_sudden_death_prompt


def _answers_are_identical(answer1: list, answer2: list) -> bool:
    """Check if two answers are identical."""
    if answer1 is None or answer2 is None:
        return False
    try:
        return str(answer1) == str(answer2)
    except:
        return False


def _parse_grids_from_response(response: str, num_expected: int) -> Optional[List]:
    """
    Parse 2D grids from the LLM response.
    
    Tries multiple parsing strategies:
    1. JSON block with ```json ... ``` containing {"answers": [...]}
    2. Raw JSON object with "answers" key
    3. Single grid (for backward compatibility)
    
    Args:
        response: The LLM response string
        num_expected: Number of grids expected (1, 2, or 3)
    
    Returns:
        List of 2D grids, or None if parsing fails
    """
    if not response:
        return None
    
    # Strategy 1: Look for ```json ... ``` block with "answers" key
    json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group(1))
            if isinstance(data, dict) and "answers" in data:
                answers = data["answers"]
                if isinstance(answers, list) and len(answers) >= num_expected:
                    return answers[:num_expected]
            # Fallback: single answer key
            if isinstance(data, dict) and "answer" in data:
                return [data["answer"]]
        except json.JSONDecodeError:
            pass
    
    # Strategy 2: Look for raw JSON object with "answers" key
    json_obj_match = re.search(r'\{[^{}]*"answers"\s*:\s*\[.*?\]\s*\}', response, re.DOTALL)
    if json_obj_match:
        try:
            data = json.loads(json_obj_match.group(0))
            if isinstance(data, dict) and "answers" in data:
                answers = data["answers"]
                if isinstance(answers, list) and len(answers) >= num_expected:
                    return answers[:num_expected]
        except json.JSONDecodeError:
            pass
    
    # Strategy 3: Look for raw JSON object with single "answer" key
    json_single_match = re.search(r'\{[^{}]*"answer"\s*:\s*\[.*?\]\s*\}', response, re.DOTALL)
    if json_single_match:
        try:
            data = json.loads(json_single_match.group(0))
            if isinstance(data, dict) and "answer" in data:
                return [data["answer"]]
        except json.JSONDecodeError:
            pass
    
    # Strategy 4: Look for any 2D array pattern [[...], [...], ...]
    # This might catch a single grid
    array_match = re.search(r'\[\s*\[[\d,\s]+\](?:\s*,\s*\[[\d,\s]+\])*\s*\]', response, re.DOTALL)
    if array_match:
        try:
            import ast
            grid = ast.literal_eval(array_match.group(0))
            if isinstance(grid, list) and len(grid) > 0:
                # Check if it's a single grid or list of grids
                if isinstance(grid[0], list) and len(grid[0]) > 0:
                    if isinstance(grid[0][0], int):
                        # It's a single 2D grid
                        return [grid]
                    elif isinstance(grid[0][0], list):
                        # It's a list of grids
                        return grid[:num_expected]
        except (ValueError, SyntaxError):
            pass
    
    return None


async def _run_sudden_death(
    training_examples: list,
    test_inputs: list,
    current_answers: list,
    winning_code: str,
    num_test_inputs: int,
) -> tuple[list, bool]:
    """
    Run sudden death round to produce alternative answer(s).
    
    Asks LLM for DIRECT 2D grid answer(s) (not Python code).
    Uses retry logic to ensure we always get an answer.
    Supports multiple test inputs.
    
    Args:
        training_examples: List of training input/output pairs
        test_inputs: List of ALL test input grids
        current_answers: List of current answers (one per test input)
        winning_code: The code that produced current answers
        num_test_inputs: Number of test inputs (1, 2, or 3)
    
    Returns:
        Tuple of (alternative_answers, success) where alternative_answers is a list of grids
    """
    print(f"\n   {'='*60}")
    print(f"   ⚡ SUDDEN DEATH: Requesting {num_test_inputs} alternative grid(s)...")
    print(f"   {'='*60}")
    
    MAX_RETRIES = 3
    RETRY_BACKOFF = 5  # seconds
    
    alt_answers = None
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            prompt = build_sudden_death_prompt(
                training_examples=training_examples,
                test_inputs=test_inputs,
                current_answers=current_answers,
                winning_code=winning_code,
            )
            
            # Add extra emphasis on retries
            if attempt > 1:
                prompt += f"\n\n⚠️ RETRY {attempt}/{MAX_RETRIES}: Your previous answer was invalid or identical to Attempt 1. YOU MUST produce {num_test_inputs} DIFFERENT, VALID 2D grid(s)!"
            
            # Call Gemini for sudden death
            response = await call_gemini_pro(prompt, context=f"Sudden Death (attempt {attempt})")
            
            if not response:
                print(f"   ⚠️ Sudden death attempt {attempt}: No response from LLM")
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_BACKOFF)
                continue
            
            # Parse the 2D grid(s) directly from response
            alt_answers = _parse_grids_from_response(response, num_test_inputs)
            
            if alt_answers is None or len(alt_answers) < num_test_inputs:
                print(f"   ⚠️ Sudden death attempt {attempt}: Could not parse {num_test_inputs} grid(s) from response")
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_BACKOFF)
                continue
            
            # Check if ALL answers are different from current
            if _answers_are_identical(alt_answers, current_answers):
                print(f"   ⚠️ Sudden death attempt {attempt}: Produced identical answer(s), retrying...")
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_BACKOFF)
                continue
            
            # Success! We have different answer(s)
            print(f"   ✅ Sudden death: Got {len(alt_answers)} different answer(s) on attempt {attempt}!")
            return alt_answers, True
            
        except Exception as e:
            print(f"   ⚠️ Sudden death attempt {attempt} error: {e}")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BACKOFF)
            continue
    
    # All retries exhausted - return whatever we got last (even if same or partial)
    print(f"   ⚠️ Sudden death: All {MAX_RETRIES} attempts exhausted, using last parsed answer")
    if alt_answers is not None and len(alt_answers) > 0:
        # Pad with copies if we don't have enough grids
        while len(alt_answers) < num_test_inputs:
            alt_answers.append(alt_answers[-1])
        return alt_answers, True
    else:
        # Absolute fallback - couldn't parse anything
        print(f"   ❌ Sudden death: Could not produce any valid answer")
        return None, False


async def execute_step_4(combined_result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute Step 4: Format answers for API submission.
    
    Uses top solution for Attempt 1, and second distinct solution for Attempt 2 (if available).
    If both attempts would be identical, triggers SUDDEN DEATH to get different answer(s).
    Supports questions with multiple test inputs.
    
    Args:
        combined_result: Contains python_answers, python_answers_2 (optional), and metadata
    
    Returns:
        Dict with formatted_answer ready for API submission
    """
    print(f"\n{'='*70}")
    print(f"📦 STEP 4: Format Answers for Submission")
    print(f"{'='*70}")
    
    python_answers = combined_result.get("python_answers", [])
    python_answers_2 = combined_result.get("python_answers_2", None)
    python_has_answer = combined_result.get("python_has_answer", False)
    python_has_winner = combined_result.get("python_has_winner", False)
    num_test_inputs = combined_result.get("num_test_inputs", 1)
    
    print(f"   📊 Python path: {'✅ 100% winner' if python_has_winner else '⚠️ Best available' if python_has_answer else '❌ No answer'}")
    print(f"   📊 Test inputs: {num_test_inputs}")
    
    # Check if we have two different answers or just one
    has_distinct_second = python_answers_2 and not _answers_are_identical(python_answers, python_answers_2)
    
    if has_distinct_second:
        print(f"   🔀 Using distinct second solution for Attempt 2")
    elif python_has_answer and not has_distinct_second:
        # All islands produced identical answers - trigger SUDDEN DEATH
        print(f"   ⚠️ All islands produced identical answers!")
        
        # Get training examples and test inputs from combined_result
        training_examples = combined_result.get("train_examples", combined_result.get("training_examples", []))
        test_inputs = combined_result.get("test_inputs", [])
        winning_code = ""
        
        # Extract winning code from top_result
        top_result = combined_result.get("top_result")
        if top_result:
            train_results = top_result.get("train_results", [])
            if train_results:
                winning_code = train_results[0].get("code", "")
        
        # Run sudden death with ALL test inputs
        alt_answers, success = await _run_sudden_death(
            training_examples=training_examples,
            test_inputs=test_inputs,
            current_answers=python_answers,
            winning_code=winning_code,
            num_test_inputs=num_test_inputs,
        )
        
        if success and alt_answers:
            python_answers_2 = alt_answers
            print(f"   ✅ Using sudden death alternative(s) for Attempt 2")
    
    formatted_answer, has_answer, attempt_1_source, attempt_2_source = format_answers(
        python_answers,
        python_has_answer,
        python_has_winner,
        num_test_inputs,
        python_answers_2=python_answers_2
    )
    
    print(f"   ✅ Attempt 1: {attempt_1_source}")
    print(f"   ✅ Attempt 2: {attempt_2_source}")
    print(f"   📤 Formatted {len(formatted_answer)} answer(s) for submission")
    
    return {
        **combined_result,
        "formatted_answer": formatted_answer,
        "has_answer": has_answer,
        "attempt_1_source": attempt_1_source,
        "attempt_2_source": attempt_2_source
    }
