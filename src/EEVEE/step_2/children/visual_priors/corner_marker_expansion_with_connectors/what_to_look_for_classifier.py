CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER MARKER EXPANSION WITH CONNECTING LINES?

This pattern involves:
- The input has exactly 4 non-zero cells arranged as corners of a rectangle (2 pairs of matching colors diagonally opposite)
- Each corner marker is expanded into a 3x3 block in the output
- The 3x3 block has the OPPOSITE color as its border and the ORIGINAL color at its center
- A connector color (typically gray/neutral) is used to:
  1. Draw dotted/dashed lines between the two corner markers on the same row
  2. Draw vertical lines between corner markers in the same column
- The corner pairs are swapped: where color A was, color B's border appears (and vice versa)

Look at the training examples:
- Are there exactly 4 isolated non-zero cells forming rectangle corners?
- Do the corners come in 2 pairs of matching colors placed diagonally?
- In the output, does each corner become a 3x3 block with swapped border/center colors?
- Are there connector lines (using a third color) between the corners?

Answer ONLY with: YES or NO"""
