CLASSIFIER_PROMPT = """Does this puzzle exhibit a BOUNCING DIAGONAL LINE pattern?

A bouncing diagonal line pattern means:
- The input is mostly empty (background color) with a single non-zero cell in the bottom-left corner
- The output has the same dimensions as the input
- A diagonal line of the non-zero color "bounces" back and forth across the grid
- The line starts from the position of the non-zero cell and moves diagonally upward
- When the line reaches either the left or right edge, it reflects/bounces and continues in the opposite diagonal direction
- This creates a zigzag pattern moving from bottom to top

Look at the training examples:
- Is there exactly one non-zero cell in the input, located at the bottom-left?
- Does the output show a single diagonal path that bounces off the left and right edges?
- Does the path traverse from the bottom row to the top row?
- Is there exactly one non-zero cell per row in the output?

Answer ONLY with: YES or NO"""
