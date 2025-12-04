CLASSIFIER_PROMPT = """Does this puzzle exhibit STRAY MARKER ATTRACTION TO DIVIDING LINES?

This pattern involves:
- One or more straight lines (horizontal or vertical) that span the entire grid, acting as dividers
- Scattered "stray" markers of the SAME color as a dividing line, located elsewhere in the grid
- The transformation moves these stray markers to be adjacent to their corresponding dividing line

Look at the training examples:
- Are there continuous lines (horizontal or vertical) that divide the grid into regions?
- Are there isolated single cells with the same color as one of these dividing lines?
- In the output, do these isolated markers disappear from their original positions?
- Do the dividing lines gain an extra cell adjacent to them at the same row/column as where the stray marker was?

The key insight: stray markers are "attracted" to their matching dividing line - they move to touch the line while preserving their row (for vertical lines) or column (for horizontal lines).

Answer ONLY with: YES or NO"""
