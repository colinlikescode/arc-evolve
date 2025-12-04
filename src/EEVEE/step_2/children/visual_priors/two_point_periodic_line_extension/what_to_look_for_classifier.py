CLASSIFIER_PROMPT = """Does this puzzle exhibit TWO-POINT PERIODIC LINE EXTENSION?

This pattern involves:
- The input grid is mostly empty (background color) with exactly TWO non-zero colored cells
- These two cells define a periodic pattern that gets extended across the grid
- The extension direction depends on the relative positions of the two points:
  - If the points are in different ROWS but could define VERTICAL stripes: extend vertically (fill entire columns)
  - If the points are in different COLUMNS but could define HORIZONTAL stripes: extend horizontally (fill entire rows)
- The pattern created by the two points repeats periodically across the grid

Look at the training examples:
- Are there exactly two non-zero cells in the input?
- Does the output show lines (rows or columns) filled with alternating colors?
- Does the spacing between the two original points define the period of repetition?
- Are the lines extended in one direction (either all horizontal or all vertical)?

Answer ONLY with: YES or NO"""
