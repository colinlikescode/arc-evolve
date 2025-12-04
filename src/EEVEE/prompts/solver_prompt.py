"""
Main solver prompt with visual prior hints.

Enhanced prompt with prominent hint display and boxed headers.
"""


def _get_step2_formulate() -> str:
    """Get the STEP 2: Formulate Hypothesis section."""
    return """╔══════════════════════════════════════════════════════════════╗
║              STEP 2: FORMULATE YOUR HYPOTHESIS               ║
╚══════════════════════════════════════════════════════════════╝

Based on your analysis, formulate a transformation rule that works consistently across all examples.

• Express the rule as a sequence of image manipulation operations
• Prioritize simpler rules first
• Consider these types of transformations:
  - Object Manipulation: Moving, rotating, reflecting, or resizing objects
  - Color Changes: Changing the color of specific objects or regions
  - Spatial Arrangements: Rearranging the objects in a specific pattern
  - Object Addition/Removal: Adding or removing objects based on certain criteria

Do not move onto step 3, until step 2 is fully complete."""


def build_solver_prompt(problem_str: str, pattern_hints: str = "") -> str:
    """
    Build the main solver prompt.
    
    Args:
        problem_str: Formatted problem with examples and test inputs
        pattern_hints: Visual prior hints (inserted directly like old codebase)
    
    Returns:
        Complete prompt string
    """
    # Get step 2 content (will be replaced with feedback if available)
    step2_content = _get_step2_formulate()
    
    base_prompt = f'''You are the world champion of solving Abstract Reasoning Corpus (ARC) tasks by writing Python code. Your task is to study the input–output pairs and write a transform function that reliably converts any input grid into its correct output.
{pattern_hints}

╔══════════════════════════════════════════════════════════════╗
║                      TODAY'S QUESTION                        ║
╚══════════════════════════════════════════════════════════════╝

Below is a textual representation of the input-output examples and the challenge to be solved.

{problem_str}

╔══════════════════════════════════════════════════════════════╗
║          STEP 1: STUDY EVERY SINGLE EXAMPLE PAIR            ║
╚══════════════════════════════════════════════════════════════╝

Compare all training examples:

• Study each example input → output transformation carefully
• Identify the key objects in the input and output grids (e.g., shapes, lines, regions)
• Determine the relationships between these objects (e.g., spatial arrangement, color, size)
• Identify the operations that transform the input objects and relationships into the output objects and relationships (e.g., rotation, reflection, color change, object addition/removal)
• Consider the grid dimensions, symmetries, and other visual features
• Explain what each example transformation has in common out loud

Do not move onto step 2, until step 1 is fully complete.

{step2_content}

╔══════════════════════════════════════════════════════════════╗
║              STEP 3: STUDY THE TEST INPUT                   ║
╚══════════════════════════════════════════════════════════════╝

Make sure that your transformation rule has not overfit to the training examples and will work on the test input.

• Play devil's advocate and steelman why your rule won't work
• Consider edge cases and variations
• Refine your hypothesis until it is stronger and more generalizable
• Make sure that you're not developing a false positive that only works on the training examples

If you answered BAD to any question, your rule is OVERFITTING. Go back to Step 2.

Do not move onto step 4, until step 3 is fully complete.

╔══════════════════════════════════════════════════════════════╗
║            STEP 4: VERIFY (MANDATORY - DO NOT SKIP)          ║
╚══════════════════════════════════════════════════════════════╝

You MUST verify your transformation rule follows the EXACT SAME pattern as all training examples.

VERIFICATION STRUCTURE:

1. List each training example and test if your transformation rule applies:
   - Input: [show input grid]
   - Close your eyes and forget about the real output
   - Expected Output: [apply your transformation rule against the input]
   - Real Output: [now check against the real output example]
   - ✓ Pattern matches or ✗ Pattern does not match

2. You must pass ALL training examples with your transformation rule before moving onto step 5.
   If you fail, return to step 2 and refine your hypothesis.

Do not move onto step 5, until step 4 is fully complete.

╔══════════════════════════════════════════════════════════════╗
║         STEP 5: IMPLEMENT CODE (REQUIRED - DO NOT SKIP)      ║
╚══════════════════════════════════════════════════════════════╝

Write a Python function called arc_transform that implements your transformation rule.

REQUIREMENTS:

• Function signature: def arc_transform(grid: list[list[int]]) -> list[list[int]]:
• The function takes a grid (list of lists of ints 0-9) and returns the transformed grid
• Use standard Python libraries (NumPy is available if needed)
• Write modular code with clear variable names and comments
• Document your code clearly, explaining the transformation rule in the docstring
• Handle edge cases and invalid inputs gracefully

⚠️ CRITICAL: YOUR CODE MUST BE UNIVERSAL ⚠️

Your code will be tested on UNSEEN inputs. It MUST work on ANY valid input, not just the examples shown.

FORBIDDEN PATTERNS (these will FAIL on test inputs):
• ❌ Hardcoded grid sizes: if grid.shape == (5, 5) or if len(grid) == 3
• ❌ Hardcoded positions: if grid[2][3] == 5 or grid[0][0] == 1
• ❌ Hardcoded colors: if color == 3 (unless the rule explicitly involves that color)
• ❌ Example-specific conditions: any if-statement checking for specific values from training examples
• ❌ Lookup tables mapping specific inputs to outputs
• ❌ Multiple if-else branches handling each example separately

REQUIRED PATTERNS (these generalize correctly):
• ✓ Detect patterns dynamically: find objects, measure sizes, identify colors at runtime
• ✓ Use relative positions: center of grid, bounding box of object, etc.
• ✓ Apply transformations uniformly: same operation on all objects of a type
• ✓ Derive parameters from input: grid dimensions, object locations, dominant colors

ASK YOURSELF: "If I gave this code a completely new grid it's never seen, would it still work?"
If the answer is no, your code is overfitting and will fail.

OUTPUT FORMAT:

Provide exactly 3 different solutions, each with step-by-step instructions and code.
Your first solution should be your most confident answer.
Solutions 2 and 3 should explore genuinely different interpretations or approaches.

Format each solution as:
<solution_1>
<instructions>
[step-by-step instructions]
</instructions>
```python
[code]
```
</solution_1>

<solution_2>
<instructions>
[step-by-step instructions]
</instructions>
```python
[code]
```
</solution_2>

<solution_3>
<instructions>
[step-by-step instructions]
</instructions>
```python
[code]
```
</solution_3>

───────────────────────────────────────────────────────────────
                     REFERENCE EXAMPLES
───────────────────────────────────────────────────────────────

EXAMPLE 1:

Input:
[[2, 2, 2],
 [2, 0, 2],
 [2, 2, 2]]

Output:
[[0, 0, 0],
 [0, 2, 0],
 [0, 0, 0]]

<instructions>
1. Create a new grid filled with zeros
2. Copy only the interior cells (not the border) from the input to the output
3. The border becomes 0, the center keeps its original value
</instructions>

```python
import numpy as np

def arc_transform(grid: np.ndarray) -> np.ndarray:
    """Swap border and center - border becomes 0, center preserved."""
    result = np.zeros_like(grid)
    if grid.shape[0] > 2 and grid.shape[1] > 2:
        result[1:-1, 1:-1] = grid[1:-1, 1:-1]
    return result
```

EXAMPLE 2:

Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
[[9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]]

<instructions>
1. Flip the grid vertically (reverse row order)
2. Flip the result horizontally (reverse column order)
3. This is equivalent to a 180-degree rotation
</instructions>

```python
import numpy as np

def arc_transform(grid: np.ndarray) -> np.ndarray:
    """Rotate grid 180 degrees by flipping both axes."""
    return np.flip(np.flip(grid, axis=0), axis=1)
```

EXAMPLE 3:

Input:
[[0, 0, 0, 0, 0],
 [0, 3, 3, 3, 0],
 [0, 3, 0, 3, 0],
 [0, 3, 3, 3, 0],
 [0, 0, 0, 0, 0]]

Output:
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 3, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]

<instructions>
1. Find the hollow rectangle pattern made of 3s
2. Identify the center cell of the grid
3. Create a new grid filled with zeros
4. Copy only the center cell value to the output
</instructions>

```python
import numpy as np

def arc_transform(grid: np.ndarray) -> np.ndarray:
    """Extract center value from hollow rectangle pattern."""
    rows, cols = grid.shape
    result = np.zeros_like(grid)
    center_r, center_c = rows // 2, cols // 2
    result[center_r, center_c] = grid[center_r, center_c]
    return result
```
'''
    
    return base_prompt
