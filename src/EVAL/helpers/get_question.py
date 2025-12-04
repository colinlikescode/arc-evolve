import httpx
import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


async def get_question(question_id: int, dataset: str = "arc-agi-1") -> Dict[str, Any]:
    """
    Get a question from the ARC-AGI API.
    
    Args:
        question_id: The ID of the question to fetch
        dataset: The dataset name ("arc-agi-1" or "arc-agi-2")
    
    Returns:
        Dictionary containing the question data
    """
    railway_endpoint = os.getenv("RAILWAY_API_ENDPOINT")
    if not railway_endpoint:
        raise ValueError("RAILWAY_API_ENDPOINT environment variable is required")
    url = f"{railway_endpoint}/question"
    
    payload = {
        "question_id": question_id,
        "dataset": dataset
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


async def ping_and_get_question(question_id: int, dataset: str = "arc-agi-1") -> Dict[str, Any]:
    """
    Step 1: Ping the API to get the question.
    
    Args:
        question_id: The ID of the question to fetch
        dataset: The dataset name ("arc-agi-1" or "arc-agi-2")
    
    Returns:
        Dictionary containing question data with train_examples and test_inputs
    """
    print(f"Step 1: Getting question {question_id} from dataset {dataset}")
    
    try:
        question_data = await get_question(question_id, dataset)
        print(f"✓ Successfully retrieved question {question_id}")
        print(f"  - Dataset: {question_data['dataset']}")
        print(f"  - Train examples: {len(question_data['train_examples'])}")
        print(f"  - Test inputs: {len(question_data['test_inputs'])}")
        return question_data
    except Exception as e:
        print(f"✗ Error getting question: {e}")
        raise

