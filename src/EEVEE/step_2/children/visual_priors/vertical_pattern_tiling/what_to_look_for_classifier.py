CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL PATTERN TILING from a repeating unit?

This pattern type means:
- The input contains a small repeating pattern (a "tile" or "unit") made of non-zero cells, typically spanning only a few consecutive rows
- The rest of the input grid is filled with background (zero) cells
- The output fills the ENTIRE grid by repeating/tiling this pattern vertically
- The pattern repeats continuously from top to bottom, covering all rows

Look at the training examples:
- Is there a localized horizontal band of non-zero cells in the input?
- Does the output tile this band pattern vertically to fill the entire grid?
- Does the horizontal pattern (columns) stay the same while the vertical pattern repeats?
- Is the output the same size as the input, just with the pattern repeated vertically?

Answer ONLY with: YES or NO"""
