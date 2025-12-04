CLASSIFIER_PROMPT = """Does this puzzle exhibit TWO-MARKER HORIZONTAL BAND DIVISION?

This pattern means:
- The input contains exactly TWO non-zero colored cells on an otherwise empty (zero) background
- One marker appears in the upper portion of the grid, one in the lower portion
- The output divides the grid into two horizontal bands/regions based on the row positions of these markers
- Each band is "owned" by its respective marker color
- Within each band, the marker's row gets a full horizontal line of that color
- The edges (first and last columns) of each band are filled with the band's color
- The interior cells remain as background (zeros)

Look at the training examples:
- Are there exactly two non-zero cells in each input?
- Is the output divided into two horizontal regions?
- Does each region have its borders/edges colored with one of the marker colors?
- Does each marker's row become a full horizontal line?

Answer ONLY with: YES or NO"""
