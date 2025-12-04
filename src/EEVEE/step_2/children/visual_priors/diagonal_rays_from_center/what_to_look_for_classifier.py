CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL EXPANSION FROM A CENTER POINT?

This pattern involves:
- The input is a square grid filled mostly with a single dominant color
- There is exactly ONE cell with a different value (typically zero/black) somewhere in the grid
- The output has the same dimensions as the input
- In the output, the different-colored cell acts as a CENTER POINT
- DIAGONAL LINES extend outward from this center point in all four diagonal directions (both main diagonals)
- The diagonal lines are marked with the same different color (zero/black)
- The rest of the grid retains the dominant color

Look at the training examples:
- Is there a single "marker" cell (different from the background) in the input?
- Does the output show diagonal lines (X pattern) emanating from that marker position?
- Do the diagonals extend to the edges/corners of the grid?

Answer ONLY with: YES or NO"""
