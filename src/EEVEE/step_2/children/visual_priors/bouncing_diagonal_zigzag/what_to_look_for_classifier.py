CLASSIFIER_PROMPT = """Does this puzzle exhibit a BOUNCING DIAGONAL / ZIGZAG PATTERN?

A bouncing diagonal pattern means:
- The input is mostly filled with background (zero) cells
- There is a single non-zero marker cell that indicates the starting position of a diagonal
- The output fills the entire grid with two colors: a fill color and the marker color
- The marker color traces a diagonal path that "bounces" off the left and right edges
- As you move row by row, the diagonal position shifts, reversing direction when it hits an edge
- This creates a zigzag or wave-like diagonal pattern across the grid

Look at the training examples:
- Is the input mostly zeros with one non-zero cell (typically in a corner)?
- Does the output show a single diagonal line that bounces/reflects at the edges?
- Does the pattern repeat vertically based on the grid width?
- Are there exactly two colors in the output (the marker color and a fill color)?

Answer ONLY with: YES or NO"""
