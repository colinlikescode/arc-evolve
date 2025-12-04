import httpx
import asyncio
import random
import os
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()


async def submit_answer(
    question_id: int,
    dataset: str,
    attempt_1: List[List[List[int]]],
    attempt_2: Optional[List[List[List[int]]]] = None,
    max_retries: int = 5
) -> Dict[str, Any]:
    """
    Submit answer to the ARC-AGI API with retry logic for transient errors.
    
    Handles 502 Bad Gateway, 503 Service Unavailable, and 429 Rate Limit errors
    with exponential backoff (2-20 seconds).
    
    Args:
        question_id: The ID of the question
        dataset: The dataset name ("arc-agi-1" or "arc-agi-2") 
        attempt_1: First attempt solution
        attempt_2: Optional second attempt solution
        max_retries: Maximum number of retry attempts
    
    Returns:
        Dictionary containing submission results
    
    Raises:
        httpx.HTTPStatusError: If all retries fail or error is not retryable
    """
    railway_endpoint = os.getenv("RAILWAY_API_ENDPOINT")
    if not railway_endpoint:
        raise ValueError("RAILWAY_API_ENDPOINT environment variable is required")
    url = f"{railway_endpoint}/answer"
    
    payload = {
        "question_id": question_id,
        "dataset": dataset,
        "attempt_1": attempt_1
    }
    
    if attempt_2 is not None:
        payload["attempt_2"] = attempt_2
    
    for attempt in range(max_retries + 1):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    json=payload,
                    timeout=30.0
                )
                
                # Handle retryable errors
                if response.status_code in (502, 503, 429):
                    if attempt < max_retries:
                        # Exponential backoff: 2^attempt seconds, capped at 20 seconds
                        backoff = min(2 ** attempt, 20.0)
                        # Add small random jitter (0-2 seconds) to avoid thundering herd
                        jitter = random.uniform(0.0, 2.0)
                        wait_time = backoff + jitter
                        print(f"   ⚠️ API error {response.status_code} on submission, retry {attempt + 1}/{max_retries} after {wait_time:.1f}s...", flush=True)
                        await asyncio.sleep(wait_time)
                        continue
                    else:
                        # Out of retries, raise the error
                        response.raise_for_status()
                
                # Success or non-retryable error
                response.raise_for_status()
                return response.json()
                
        except httpx.HTTPStatusError as e:
            # Check if it's a retryable error
            if e.response.status_code in (502, 503, 429) and attempt < max_retries:
                # Exponential backoff: 2^attempt seconds, capped at 20 seconds
                backoff = min(2 ** attempt, 20.0)
                jitter = random.uniform(0.0, 2.0)
                wait_time = backoff + jitter
                print(f"   ⚠️ API error {e.response.status_code} on submission, retry {attempt + 1}/{max_retries} after {wait_time:.1f}s...", flush=True)
                await asyncio.sleep(wait_time)
                continue
            else:
                # Non-retryable error or out of retries
                raise
        except Exception as e:
            # For other errors (network, timeout, etc.), retry with backoff
            if attempt < max_retries:
                backoff = min(2 ** attempt, 20.0)
                jitter = random.uniform(0.0, 2.0)
                wait_time = backoff + jitter
                print(f"   ⚠️ Error submitting answer, retry {attempt + 1}/{max_retries} after {wait_time:.1f}s: {str(e)[:80]}", flush=True)
                await asyncio.sleep(wait_time)
                continue
            else:
                raise
    
    # Should never reach here, but just in case
    raise Exception("Failed to submit answer after all retries")


async def submit_solution(
    question_data: Dict[str, Any],
    solutions: List[List[List[int]]],
    backup_solution: Optional[List[List[List[int]]]] = None
) -> Dict[str, Any]:
    """
    Step 3: Submit the solution from step 2.
    
    Args:
        question_data: Original question data containing question_id and dataset
        solutions: Primary solution from LLM
        backup_solution: Optional backup/alternative solution
    
    Returns:
        Dictionary containing submission results
    """
    print("Step 3: Submitting answer")
    
    question_id = question_data["question_id"]
    dataset = question_data["dataset"]
    
    try:
        result = await submit_answer(
            question_id=question_id,
            dataset=dataset,
            attempt_1=solutions,
            attempt_2=backup_solution
        )
        
        print(f"✓ Answer submitted for question {question_id}")
        print(f"  - Correct: {result.get('correct', False)}")
        print(f"  - Attempt 1 correct: {result.get('attempt_1_correct', False)}")
        
        if "attempt_2_correct" in result:
            print(f"  - Attempt 2 correct: {result.get('attempt_2_correct', False)}")
        
        return result
    
    except Exception as e:
        print(f"✗ Error submitting answer: {e}")
        raise

