"""Scoring utilities for evaluating code outputs."""
import json
import numpy as np
from typing import Optional


def soft_score(pred: np.ndarray, truth: np.ndarray) -> float:
    """
    Compute soft score (element-wise accuracy).
    
    Returns float in [0.0, 1.0] indicating percentage of correct cells.
    """
    if pred.shape != truth.shape:
        return 0.0
    if truth.size == 0:
        return 1.0
    raw = np.mean(pred == truth)
    return float(np.nan_to_num(raw, posinf=0.0, neginf=0.0))


def json_to_ndarray(s: str) -> Optional[np.ndarray]:
    """
    Parse JSON string into numpy array.
    
    Expands to 2D if needed.
    """
    try:
        obj = json.loads(s)
        arr = np.array(obj)
        if arr.ndim < 2:
            arr = np.expand_dims(arr, axis=list(range(2 - arr.ndim)))
        return arr.astype(int, copy=False)
    except Exception:
        return None


def parse_json_array_no_expand(s: str) -> Optional[np.ndarray]:
    """Parse JSON into numpy array without changing rank or dtype."""
    try:
        return np.array(json.loads(s))
    except Exception:
        return None


def grid_diff_visualization(arr1: np.ndarray, arr2: np.ndarray) -> str:
    """
    Create ASCII diff visualization.
    
    Shows matching values as-is, mismatches as 'pred/truth'.
    """
    rows, cols = arr1.shape
    out = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if arr1[i, j] == arr2[i, j]:
                row.append(str(int(arr1[i, j])))
            else:
                row.append(f"{int(arr1[i, j])}/{int(arr2[i, j])}")
        out.append(" ".join(row))
    return "\n".join(out)

