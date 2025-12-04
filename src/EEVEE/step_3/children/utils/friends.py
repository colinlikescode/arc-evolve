"""
Shared utilities for solvers.

Extracted to avoid circular imports between single_solver and collapse_booster.
"""
import re
import string
from typing import Optional
import numpy as np

from ..types.island_types import Solution


def extract_code(response: str) -> Optional[str]:
    """Extract Python code from LLM response. Takes the LONGEST code block."""
    matches = re.findall(r"```python\s*(.*?)```", response, re.DOTALL | re.IGNORECASE)
    if not matches:
        return None
    # Return the longest match (most complete code)
    return max(matches, key=len)


def extract_instructions(response: str) -> str:
    """Extract step-by-step instructions from <instructions> tags."""
    match = re.search(r"<instructions>(.*?)</instructions>", response, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_all_solutions(response: str) -> list[tuple[str, str]]:
    """
    Extract all solutions from response. Returns list of (instructions, code) tuples.
    Tries <solution_N> tags first, falls back to finding all code blocks.
    """
    solutions = []
    
    # Try to extract from <solution_N> tags
    for i in range(1, 4):
        pattern = rf"<solution_{i}>(.*?)</solution_{i}>"
        match = re.search(pattern, response, re.DOTALL | re.IGNORECASE)
        if match:
            block = match.group(1)
            instr = extract_instructions(block)
            code = extract_code(block)
            if code:
                solutions.append((instr, code))
    
    # Fallback: if no solution tags, extract all code blocks
    if not solutions:
        codes = re.findall(r"```python\s*(.*?)```", response, re.DOTALL | re.IGNORECASE)
        instrs = re.findall(r"<instructions>(.*?)</instructions>", response, re.DOTALL | re.IGNORECASE)
        for i, code in enumerate(codes):
            instr = instrs[i].strip() if i < len(instrs) else ""
            solutions.append((instr, code))
    
    return solutions


def create_solution_examples(previous_solutions: list[Solution], max_examples: int = 3, ascending_score_order: bool = False) -> str:
    """Create formatted examples from previous solutions."""
    template = string.Template("""
<previous_attempt_$index>
<instructions>
$explanation
</instructions>
```python
$code
```
<evaluation>
$feedback
</evaluation>
<score>$score</score>
</previous_attempt_$index>
""")
    if not previous_solutions:
        return ""
    
    # Extract scores and create index mapping
    solution_scores = [sol["score"] for sol in previous_solutions]
    # Sort indices by score descending
    sorted_indices = np.argsort(solution_scores)[::-1]
    # Limit to max_examples
    num_to_show = min(max_examples, len(sorted_indices))
    selected_indices = sorted_indices[:num_to_show]
    
    # Reverse order if showing ascending (worst to best)
    if ascending_score_order:
        selected_indices = selected_indices[::-1]
    
    formatted_blocks: list[str] = []
    for block_num, solution_idx in enumerate(selected_indices, start=1):
        solution = previous_solutions[solution_idx]
        # Ensure solution is a dict (Solution TypedDict behaves as dict at runtime)
        if not isinstance(solution, dict):
            print(f"   ⚠️ Warning: solution is not a dict: {type(solution)}, skipping...")
            continue
        formatted_blocks.append(
            template.substitute(
                index=block_num,
                explanation=solution.get("explanation", ""),
                code=solution.get("code", ""),
                feedback=solution.get("feedback", ""),
                score=f"{solution.get('score', 0.0):.2f}",
            )
        )
    return "\n".join(formatted_blocks)

