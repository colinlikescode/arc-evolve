"""
Detect questions with multiple test inputs.

ARC-AGI questions can have 1, 2, or 3 test inputs (never more).
"""
from typing import Dict, Any


def detect_test_inputs(question_data: Dict[str, Any]) -> int:
    """
    Detect number of test inputs in question data.
    
    Args:
        question_data: Contains test_inputs and other question data
    
    Returns:
        Number of test inputs (1, 2, or 3)
    """
    test_inputs = question_data.get("test_inputs", [])
    return len(test_inputs)

