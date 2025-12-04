"""
Sudden Death Prompt: Triggered when all islands produce identical answers.

This prompt asks the LLM to produce a DIRECT 2D grid answer (not Python code)
that is DIFFERENT from the current answer, based on alternative interpretations.
Supports multiple test inputs.
"""


def build_sudden_death_prompt(
    training_examples: list,
    test_inputs: list,
    current_answers: list,
    winning_code: str = "",
) -> str:
    """
    Build the sudden death prompt for multiple test inputs.
    
    Args:
        training_examples: List of training input/output pairs
        test_inputs: List of ALL test input grids
        current_answers: List of current answers (one per test input) - Attempt 1
        winning_code: The code that produced the current answers (for context only)
    
    Returns:
        The sudden death prompt string
    """
    # Format training examples
    examples_text = ""
    for i, ex in enumerate(training_examples, 1):
        inp = ex.get("input", [])
        out = ex.get("output", [])
        examples_text += f"\n--- Training Example {i} ---\n"
        examples_text += f"Input: {inp}\n"
        examples_text += f"Output: {out}\n"
    
    # Format test inputs and current answers
    num_tests = len(test_inputs)
    test_section = ""
    current_section = ""
    
    for i, (test_input, current_answer) in enumerate(zip(test_inputs, current_answers), 1):
        test_section += f"\n--- Test Input {i} ---\n{test_input}\n"
        current_section += f"\n--- Current Answer {i} (DO NOT PRODUCE THIS) ---\n{current_answer}\n"
    
    # Build the expected response format based on number of test inputs
    if num_tests == 1:
        response_format = '{"answers": [[[row1], [row2], ...]]}'
        example_format = '{"answers": [[[0, 1, 2], [3, 4, 5], [6, 7, 8]]]}'
    else:
        response_format = '{"answers": [[[grid1_row1], ...], [[grid2_row1], ...], ...]}'
        example_format = '{"answers": [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]}'
    
    prompt = f"""
You are Korea's Top Math Olympiad, Nam Do-san.

╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  SUDDEN DEATH: PRODUCE DIFFERENT ANSWER(S)                               ║
║  Multiple attempts produced the SAME answer - we need ALTERNATIVE(S)!        ║
╚══════════════════════════════════════════════════════════════════════════════╝

SITUATION:
Multiple independent solving attempts ALL produced the EXACT SAME answer(s).
This might mean we're missing a subtle pattern variation. We need you to 
produce DIFFERENT answer(s) based on an alternative interpretation.

NUMBER OF TEST INPUTS: {num_tests}
You must provide {num_tests} answer grid(s), one for each test input.

═══════════════════════════════════════════════════════════════════════════════
TRAINING EXAMPLES (for context):
═══════════════════════════════════════════════════════════════════════════════
{examples_text}

═══════════════════════════════════════════════════════════════════════════════
TEST INPUT(S):
═══════════════════════════════════════════════════════════════════════════════
{test_section}

═══════════════════════════════════════════════════════════════════════════════
CURRENT ANSWER(S) - DO NOT PRODUCE THESE SAME GRIDS:
═══════════════════════════════════════════════════════════════════════════════
{current_section}

═══════════════════════════════════════════════════════════════════════════════
CODE THAT PRODUCED CURRENT ANSWERS (for context only):
═══════════════════════════════════════════════════════════════════════════════
```python
{winning_code if winning_code else "# Code not available"}
```

═══════════════════════════════════════════════════════════════════════════════
ALTERNATIVE PATTERNS TO CONSIDER:
═══════════════════════════════════════════════════════════════════════════════

🔄 ROTATION/REFLECTION:
   - 90°, 180°, 270° rotations
   - Horizontal or vertical flip
   - Transpose (swap rows and columns)

🎨 COLOR MUTATIONS:
   - Off-by-one color values
   - Color swapping or remapping
   - Background/foreground inversion

📐 BOUNDARY/POSITION:
   - One-pixel shifts
   - Cropping or padding differences
   - Different bounding box interpretation

🔗 CONNECTIONS:
   - Missing bridges or lines
   - Gaps that should be filled
   - Different connectivity rules

═══════════════════════════════════════════════════════════════════════════════
YOUR TASK - CRITICAL INSTRUCTIONS:
═══════════════════════════════════════════════════════════════════════════════

1. Study the training examples and current answers
2. Think about what alternative interpretation might be correct
3. Produce {num_tests} DIFFERENT answer grid(s), one for each test input

⚠️  YOUR OUTPUT GRID(S) MUST BE DIFFERENT FROM THE CURRENT ANSWER(S) ABOVE ⚠️
⚠️  DO NOT PRODUCE THE SAME GRIDS - WE ALREADY HAVE THOSE AS ATTEMPT 1      ⚠️

RESPOND WITH EXACTLY THIS JSON FORMAT (no other text):
```json
{response_format}
```

Where "answers" is a list containing {num_tests} 2D grid(s), each grid being a list of rows.
Each row is a list of integers (0-9 representing colors).

Example response format for {num_tests} test input(s):
```json
{example_format}
```

PRODUCE YOUR {num_tests} DIFFERENT ANSWER GRID(S) NOW:
"""
    return prompt
