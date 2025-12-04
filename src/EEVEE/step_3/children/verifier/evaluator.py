"""
Verifier 1: Training Evaluation

Executes code on all training examples and produces scores.
This is the main verification step that runs for every iteration.
"""
import json
import os
import subprocess
import tempfile
from typing import Optional, List, Dict, Any, Tuple


def get_grid_similarity(
    ground_truth_grid: List[List[int]], sample_grid: List[List[int]]
) -> float:
    """
    Calculate similarity as the percentage of cells that match exactly.
    Returns a value between 0.0 (no matches) and 1.0 (perfect match).
    
    Args:
        ground_truth_grid: The correct/expected grid
        sample_grid: The predicted grid to compare
    
    Returns:
        Similarity score between 0.0 and 1.0
    """
    if not ground_truth_grid or not sample_grid:
        return 0.0

    # Check if grids have the same number of rows
    if len(ground_truth_grid) != len(sample_grid):
        return 0.0
    
    # Check if ALL rows have the same length (catches jagged arrays)
    for i in range(len(ground_truth_grid)):
        if len(ground_truth_grid[i]) != len(sample_grid[i]):
            return 0.0

    rows = len(ground_truth_grid)
    cols = len(ground_truth_grid[0]) if rows > 0 else 0
    total_cells = rows * cols
    if total_cells == 0:
        return 0.0
    
    matching_cells = 0
    for i in range(rows):
        for j in range(len(ground_truth_grid[i])):
            if ground_truth_grid[i][j] == sample_grid[i][j]:
                matching_cells += 1

    return matching_cells / total_cells


def score_answer(predicted: List[List[int]], holdout: List[List[int]]) -> bool:
    """
    Score a predicted answer against the holdout output.
    
    Args:
        predicted: Predicted grid from the LLM
        holdout: Ground truth holdout output
    
    Returns:
        True if grids match exactly, False otherwise
    """
    # Check dimensions
    if len(predicted) != len(holdout):
        return False
    
    if not predicted or not holdout:
        return False
    
    if len(predicted[0]) != len(holdout[0]):
        return False
    
    # Check cell-by-cell match
    for i in range(len(predicted)):
        if len(predicted[i]) != len(holdout[i]):
            return False
        for j in range(len(predicted[i])):
            if predicted[i][j] != holdout[i][j]:
                return False
    
    return True


def _parse_output_to_grid(output_str: str) -> Optional[List[List[int]]]:
    """Parse JSON output string to grid (list of lists)."""
    try:
        obj = json.loads(output_str)
        # Convert to list of lists if needed
        if isinstance(obj, list):
            return obj
        return None
    except Exception:
        return None


def execute_code_on_input(code: str, input_grid: List[List[int]]) -> Optional[List[List[int]]]:
    """
    Execute code on a single input and return the output grid.
    
    This matches the old codebase's synchronous execution pattern.
    """
    wrapper = f'''
import json
import sys
import numpy as np

{code}

try:
    input_grid = json.loads(sys.argv[1])
    # Convert to numpy array like old codebase does
    input_array = np.array(input_grid)
    result = arc_transform(input_array)
    # Convert numpy arrays to lists if needed
    if hasattr(result, 'tolist'):
        result = result.tolist()
    print(json.dumps({{"success": True, "output": result}}))
except Exception as e:
    print(json.dumps({{"success": False, "error": str(e)}}))
'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(wrapper)
        temp_file = f.name
    
    try:
        result = subprocess.run(
            ['python3', temp_file, json.dumps(input_grid)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            try:
                output_data = json.loads(result.stdout.strip())
                if output_data.get("success"):
                    return output_data.get("output")
                else:
                    # Execution failed with error message
                    return None
            except json.JSONDecodeError:
                return None
        else:
            # Non-zero return code - log stderr for debugging
            if result.stderr:
                # Print first 500 chars of error for debugging
                error_preview = result.stderr[:500]
                if "EEVEE" in error_preview or "verifier" in error_preview:
                    print(f"⚠️  Code execution error (likely LLM hallucination): {error_preview}")
            return None
        
    except subprocess.TimeoutExpired:
        return None
    except Exception:
        return None
    finally:
        try:
            os.unlink(temp_file)
        except:
            pass


def evaluate_on_training(
    code: str,
    train_in: list[list[list[int]]],
    train_out: list[list[list[int]]],
    executor_func=None,  # Kept for backward compatibility but not used
    timeout_s: float = 5.0  # Kept for backward compatibility but not used
) -> Tuple[List[Dict[str, Any]], float, bool]:
    """
    Execute code on all training examples and build feedback.
    
    This matches the old codebase's synchronous execution pattern.
    
    Args:
        code: Python code to execute
        train_in: Training input grids
        train_out: Training output grids
        executor_func: Ignored (kept for backward compatibility)
        timeout_s: Ignored (kept for backward compatibility)
    
    Returns:
        (train_results, mean_score, all_correct)
        - train_results: List of dicts with example_idx, success, predicted, expected, similarity, error, code
        - mean_score: Mean similarity across all examples
        - all_correct: True if all examples passed
    """
    # Convert to old format: list of dicts with 'input' and 'output' keys
    training_examples = [
        {"input": inp, "output": out}
        for inp, out in zip(train_in, train_out, strict=True)
    ]
    
    results = []
    scores = []
    all_correct = True
    
    for idx, example in enumerate(training_examples):
        input_grid = example['input']
        expected_output = example['output']
        # Use synchronous execution like old codebase
        predicted = execute_code_on_input(code, input_grid)
        
        if predicted is None:
            # Execution failed
            results.append({
                "example_idx": idx + 1,
                "success": False,
                "predicted": None,
                "expected": expected_output,
                "similarity": 0.0,
                "soft_score": 0.0,  # Backward compatibility
                "error": "Execution failed or timeout",
                "output": "",  # Backward compatibility
                "code": code
            })
            scores.append(0.0)
            all_correct = False
        else:
            # Check if correct
            is_correct = score_answer(predicted, expected_output)
            similarity = get_grid_similarity(expected_output, predicted)
            
            if not is_correct:
                all_correct = False
            
            results.append({
                "example_idx": idx + 1,
                "success": is_correct,
                "predicted": predicted,
                "expected": expected_output,
                "similarity": similarity,
                "soft_score": similarity,  # Backward compatibility (alias)
                "error": None,
                "output": json.dumps(predicted),  # Backward compatibility
                "code": code
            })
            scores.append(similarity)
    
    mean_score = sum(scores) / len(scores) if scores else 0.0
    return results, mean_score, all_correct


def build_feedback_from_results(
    train_results: List[Dict[str, Any]],
    train_out: list[list[list[int]]]
) -> str:
    """
    Build feedback string from training results.
    
    Args:
        train_results: Results from evaluate_on_training
        train_out: Expected training outputs (kept for backward compatibility, but not used)
    
    Returns:
        Formatted feedback string
    """
    feedback_parts = []
    
    for r in train_results:
        idx = r.get("example_idx", 0)
        
        if r["success"]:
            feedback_parts.append(f"Solves Example #{idx} correctly.")
        elif r.get("error"):
            feedback_parts.append(f"Solves Example #{idx} incorrectly.\nError: {r['error']}")
        else:
            msg = f"Solves Example #{idx} incorrectly."
            
            if r.get("predicted") is not None and r.get("expected") is not None:
                predicted = r["predicted"]
                expected = r["expected"]
                
                pred_shape = f"{len(predicted)}x{len(predicted[0]) if predicted else 0}"
                exp_shape = f"{len(expected)}x{len(expected[0]) if expected else 0}"
                
                if pred_shape != exp_shape:
                    msg += f"\nShape mismatch: predicted {pred_shape}, expected {exp_shape}."
                else:
                    msg += f"\nYour code's output does not match the expected output."
                    similarity = r.get("similarity", 0.0)
                    msg += f"\nSimilarity: {similarity:.1%}"
            
            feedback_parts.append(msg)
    
    return "\n\n".join(feedback_parts)
