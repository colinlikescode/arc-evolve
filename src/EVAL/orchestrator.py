"""
EVAL Orchestrator - processes ARC-AGI questions through EEVEE pipeline.

1. Get question from API
2. Pass to EEVEE orchestrator
3. Submit answer
"""
import asyncio
import threading

from EVAL.helpers.get_question import get_question
from EVAL.helpers.submit_answer import submit_answer
from EVAL.config import MAX_IN_PARALLEL
from EVAL.helpers.parallel import run_parallel
from EEVEE.orchestrator import process_question as process_question_func
import os

# Thread-safe tracking of questions being processed
_processing_lock = threading.Lock()
_currently_processing = set()

print(f"✅ Using EEVEE orchestrator")

async def process_single_question(question_id: int, total_questions: int, dataset: str = "arc-agi-1", actually_submit: bool = True):
    """Process a single question through all 3 steps with automatic retry on failure"""
    
    MAX_RETRIES = 3
    last_error = None
    
    for attempt in range(1, MAX_RETRIES + 1):
        # Check if this question is already being processed
        with _processing_lock:
            if question_id in _currently_processing:
                print(f"⚠️  ERROR: Question {question_id} is already being processed! This should not happen.")
                raise ValueError(f"Question {question_id} is already being processed")
            _currently_processing.add(question_id)
        
        try:
            attempt_str = f" (attempt {attempt}/{MAX_RETRIES})" if attempt > 1 else ""
            print(f"\n📍 Question {question_id}/{total_questions}{attempt_str}")
            
            # Step 1: Get question
            question_data = await get_question(question_id, dataset)
            question_data["question_id"] = question_id
            
            # Map field names for EEVEE (API returns train_examples, EEVEE expects training_examples)
            if "train_examples" in question_data and "training_examples" not in question_data:
                question_data["training_examples"] = question_data["train_examples"]
            
            # Step 2: Process with EEVEE orchestrator
            system_result = await process_question_func(question_data)
            
            # Extract results from EEVEE pipeline
            formatted_answer = system_result.get("formatted_answer", [])
            has_answer = system_result.get("has_answer", False)
            winning_code = system_result.get("winning_code")
            
            # Log results for EEVEE orchestrator
            print("\n" + "="*60)
            if has_answer:
                print(f"VALIDATION: PASSED")
                if winning_code:
                    print(f"   Winning Code: {len(winning_code)} chars")
            else:
                print("VALIDATION: FAILED")
                print("   No valid answer generated")
            print("="*60 + "\n")
            
            # Step 3: Submit answer (if requested and we have an answer)
            submission_result = None
            attempt_1 = []
            attempt_2 = []
            
            if actually_submit and has_answer and formatted_answer:
                print(f"📤 Submitting answer to API endpoint...")
                
                # Check if this question has multiple test inputs
                num_test_inputs = system_result.get("num_test_inputs", 1)
                has_multiple_test_inputs = num_test_inputs > 1
                
                if has_multiple_test_inputs:
                    # Special case: Multiple test inputs (2, 3, etc.)
                    # formatted_answer = [answer1_test1, answer1_test2, ..., answer2_test1, answer2_test2, ...]
                    # Build attempts by grouping every N answers (since each attempt needs all test inputs)
                    answers_per_attempt = num_test_inputs
                    grouped_attempts = []
                    for i in range(0, len(formatted_answer), answers_per_attempt):
                        chunk = formatted_answer[i:i + answers_per_attempt]
                        if len(chunk) == answers_per_attempt:
                            grouped_attempts.append(chunk)
                    
                    if not grouped_attempts:
                        # Fallback - treat whatever we have as both attempts
                        # If we have partial answers, use them for both attempts
                        attempt_1 = formatted_answer[:num_test_inputs] if len(formatted_answer) >= num_test_inputs else formatted_answer
                        attempt_2 = formatted_answer[:num_test_inputs] if len(formatted_answer) >= num_test_inputs else formatted_answer
                    else:
                        # Use the first grouped attempt for BOTH submission_1 and submission_2
                        # Both must contain all test outputs: [output_test1, output_test2, ...]
                        attempt_1 = grouped_attempts[0]  # Contains all test outputs
                        attempt_2 = grouped_attempts[0]  # Same outputs for submission_2
                else:
                    # Standard case: Single test input
                    # formatted_answer = [answer1, answer2] (both are the same since we duplicate)
                    attempt_1_grid = formatted_answer[0] if len(formatted_answer) > 0 else None
                    attempt_2_grid = formatted_answer[1] if len(formatted_answer) > 1 else formatted_answer[0]
                    
                    # Wrap each grid in a list for API format
                    attempt_1 = [attempt_1_grid] if attempt_1_grid else []
                    attempt_2 = [attempt_2_grid] if attempt_2_grid else []
                
                if has_multiple_test_inputs:
                    print(f"   Attempt 1: {len(attempt_1)} grids ({num_test_inputs} test inputs)")
                    print(f"   Attempt 2: {len(attempt_2)} grids ({num_test_inputs} test inputs)")
                else:
                    if attempt_1 and attempt_1[0]:
                        print(f"   Attempt 1: {len(attempt_1[0])}×{len(attempt_1[0][0]) if attempt_1[0] else 0} grid")
                    if attempt_2 and attempt_2[0]:
                        print(f"   Attempt 2: {len(attempt_2[0])}×{len(attempt_2[0][0]) if attempt_2[0] else 0} grid")
                
                submission_result = await submit_answer(
                    question_id, 
                    dataset, 
                    attempt_1,
                    attempt_2
                )
                print(f"   Submission result: {submission_result}")
            elif has_answer:
                print(f"ℹ️  Answer generated but not submitted (actually_submit={actually_submit})")
            else:
                print(f"ℹ️  No answer to submit")
            
            # Determine if answer was correct
            is_correct = False
            if has_answer and submission_result and submission_result.get("correct", False):
                is_correct = True
            
            # Get correctness from submission result
            attempt_1_correct = None
            attempt_2_correct = None
            if submission_result:
                attempt_1_correct = submission_result.get("attempt_1_correct")
                attempt_2_correct = submission_result.get("attempt_2_correct")
            
            # Get attempt sources from system result
            attempt_1_source = system_result.get("attempt_1_source")
            attempt_2_source = system_result.get("attempt_2_source")
            
            # Print clear final status
            if is_correct:
                print(f"\n✅ QUESTION {question_id} CORRECT ✅\n")
            else:
                print(f"\n❌ QUESTION {question_id} INCORRECT ❌\n")
            
            # Success! Return the result
            return {
                "question_id": question_id,
                "dataset": dataset,
                "status": "success",
                "correct": is_correct,
                "has_answer": has_answer,
                "winning_code": winning_code,
                "submission_result": submission_result,
                "attempt_1_correct": attempt_1_correct,
                "attempt_2_correct": attempt_2_correct,
                "attempt_1_source": attempt_1_source,
                "attempt_2_source": attempt_2_source,
                "chosen_island_id": system_result.get("chosen_island_id", -1)
            }
            
        except SystemExit:
            # Re-raise SystemExit to allow debug exits to work
            raise
        except Exception as e:
            last_error = e
            error_type = type(e).__name__
            error_msg = str(e) or "No message"
            
            print(f"❌ Question {question_id} failed (attempt {attempt}/{MAX_RETRIES}): {error_type}: {error_msg}")
            
            if attempt < MAX_RETRIES:
                wait_time = 2 ** attempt  # Exponential backoff: 2, 4, 8 seconds
                print(f"   🔄 Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                # Final attempt failed - print full traceback
                print(f"   ❌ All {MAX_RETRIES} attempts exhausted for question {question_id}")
                import traceback
                print(f"Full traceback:\n{traceback.format_exc()}")
        finally:
            # Always remove from processing set when done with this attempt
            with _processing_lock:
                _currently_processing.discard(question_id)
    
    # All retries failed - return failure result
    error_type = type(last_error).__name__ if last_error else "Unknown"
    error_msg = str(last_error) if last_error else "No message"
    return {
        "question_id": question_id,
        "dataset": dataset,
        "status": "failed",
        "correct": False,
        "error": f"{error_type}: {error_msg}"
    }


async def run_orchestrator(num_questions: int = None, starting_question_number: int = 1, dataset: str = "arc-agi-1", actually_submit: bool = True, question_numbers: list = None):
    """
    Process questions with max concurrency. As one finishes, next starts immediately.
    
    Args:
        num_questions: Total number of questions to process (ignored if question_numbers is provided)
        starting_question_number: First question ID to process (ignored if question_numbers is provided)
        dataset: Dataset name (e.g., "arc-agi-1")
        actually_submit: Whether to submit answers to API
        question_numbers: Optional list of specific question IDs to process
    """
    # Use specific question numbers if provided, otherwise use range
    if question_numbers is not None and len(question_numbers) > 0:
        if isinstance(question_numbers[0], list):
            question_ids = question_numbers[0]
        else:
            question_ids = question_numbers
        print(f"🚀 Processing {len(question_ids)} questions from {dataset}")
    else:
        question_ids = [starting_question_number + i for i in range(num_questions)]
        print(f"🚀 Processing {num_questions} questions from {dataset} starting at {starting_question_number}")
    
    print(f"   Max {MAX_IN_PARALLEL} running at once (new task starts as one finishes)")

    # Clear processing set
    with _processing_lock:
        _currently_processing.clear()

    total = len(question_ids)
    
    # Create all tasks and run with concurrency limit
    tasks = [
        process_single_question(qid, total, dataset, actually_submit)
        for qid in question_ids
    ]
    
    all_results = await run_parallel(tasks, max_concurrent=MAX_IN_PARALLEL)
    
    # Summary
    successful = [r for r in all_results if isinstance(r, dict) and r.get("status") == "success"]
    correct = [r for r in all_results if isinstance(r, dict) and r.get("correct")]
    print(f"\n📊 Final Results: {len(successful)}/{total} successful, {len(correct)}/{total} correct")

    return all_results


if __name__ == "__main__":
    asyncio.run(run_orchestrator(3))
