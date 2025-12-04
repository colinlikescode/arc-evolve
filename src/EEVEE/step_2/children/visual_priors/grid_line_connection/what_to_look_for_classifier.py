CLASSIFIER_PROMPT = """Does this puzzle exhibit a GRID-BASED LINE CONNECTION pattern?

This pattern has these characteristics:
- The grid is divided into uniform cells by a separator color forming a regular grid structure
- Each cell contains either the background color OR a colored marker
- When TWO OR MORE cells in the SAME ROW contain markers of the SAME color, ALL cells BETWEEN them (inclusive) are filled with that color
- Similarly, when TWO OR MORE cells in the SAME COLUMN contain markers of the SAME color, ALL cells BETWEEN them (inclusive) are filled with that color
- The separator grid lines remain unchanged
- Isolated markers (with no matching color in the same row/column) remain unchanged

Look at the training examples:
- Is there a visible grid structure with separator lines?
- Are there colored markers scattered in different cells?
- In the output, do matching colored markers in the same row/column get "connected" by filling intermediate cells?
- Does the connection only happen horizontally or vertically (not diagonally)?

Answer ONLY with: YES or NO"""
