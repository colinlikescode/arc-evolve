CLASSIFIER_PROMPT = """Does this puzzle exhibit REFLECTION ACROSS THE MAIN DIAGONAL (transpose of off-diagonal elements)?

Look for these indicators:
- The grid is square (NxN)
- There is a consistent "marker" color along the main diagonal (where row == column)
- In the input, non-background colored cells appear BELOW the main diagonal (where row > column)
- In the output, those same colored cells have been MOVED to the REFLECTED position ABOVE the diagonal
- The reflection rule: a cell at position (row, col) moves to position (col, row)
- After transformation, the area below the diagonal becomes empty/background

Check the training examples:
- Is there a diagonal "spine" of one color from top-left to bottom-right?
- Are colored elements below this diagonal in the input?
- Do those elements appear above the diagonal in the output (at transposed positions)?

Answer ONLY with: YES or NO"""
