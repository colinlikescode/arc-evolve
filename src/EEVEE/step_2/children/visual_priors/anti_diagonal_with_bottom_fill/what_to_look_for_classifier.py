CLASSIFIER_PROMPT = """Does this puzzle exhibit a DIAGONAL LINE AND BOTTOM ROW FILL pattern?

This pattern means:
- The input has a vertical stripe of a single non-zero color along one edge (typically the left column)
- The rest of the grid is filled with background color (zeros)
- The grid is square (same number of rows and columns)

The transformation adds:
- An anti-diagonal line of a NEW color running from the top-right corner down toward the bottom-left (stopping at the vertical stripe)
- The bottom row (except the first column) is filled with ANOTHER new color

Look at the training examples:
- Is there a single colored column on one side with the rest being background?
- Does the output add a diagonal line going from top-right to bottom-left?
- Is the bottom row filled with a different color in the output?

Answer ONLY with: YES or NO"""
