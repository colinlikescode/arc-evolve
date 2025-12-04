"""
Formatter: Format answers for API submission.
"""
from typing import List, Optional


def format_answers(
    python_answers: List,
    python_has_answer: bool,
    python_has_winner: bool,
    num_test_inputs: int = 1,
    python_answers_2: List = None
) -> tuple[List, bool, str, str]:
    """
    Format answers for API submission.
    
    Uses top solution for Attempt 1, and second distinct solution for Attempt 2 (if available).
    Otherwise duplicates Attempt 1 for Attempt 2.
    
    Args:
        python_answers: List of Python answers (grids) - ONE PER TEST INPUT (top solution)
        python_has_answer: Whether Python path has an answer
        python_has_winner: Whether Python path has a perfect solution
        num_test_inputs: Number of test inputs
        python_answers_2: Optional second distinct solution (ONE PER TEST INPUT)
    
    Returns:
        Tuple of (formatted_answers, has_answer, attempt_1_source, attempt_2_source)
        formatted_answers: For multiple test inputs, this should be [answer1_test1, answer1_test2, ..., answer2_test1, answer2_test2, ...]
    """
    formatted_answers = []
    has_answer = False
    attempt_1_source = "Python"
    attempt_2_source = "Python"
    
    # CRITICAL: For multiple test inputs, python_answers should contain outputs for ALL test inputs
    # e.g., if num_test_inputs=2, python_answers = [output_for_test1, output_for_test2]
    
    # Attempt 1: Top Python answer (ALL test inputs)
    if python_has_answer and python_answers:
        # Include ALL test outputs for Attempt 1
        # python_answers should already contain one output per test input
        if len(python_answers) >= num_test_inputs:
            # We have outputs for all test inputs - add them all
            formatted_answers.extend(python_answers[:num_test_inputs])
            has_answer = True
        elif len(python_answers) > 0:
            # We have some outputs but not all - still add what we have
            formatted_answers.extend(python_answers)
            has_answer = True
    
    # Attempt 2: Second distinct solution (if available), otherwise duplicate Attempt 1
    if has_answer:
        if python_answers_2 and len(python_answers_2) >= num_test_inputs:
            # Use second distinct solution
            formatted_answers.extend(python_answers_2[:num_test_inputs])
            attempt_2_source = "Python (Island 2)"
        elif python_answers_2 and len(python_answers_2) > 0:
            # Use second solution (partial)
            formatted_answers.extend(python_answers_2)
            attempt_2_source = "Python (Island 2)"
        else:
            # Duplicate the same answers for Attempt 2
            if len(formatted_answers) >= num_test_inputs:
                formatted_answers.extend(formatted_answers[:num_test_inputs])
            else:
                formatted_answers.extend(formatted_answers)
    
    return formatted_answers, has_answer, attempt_1_source, attempt_2_source

