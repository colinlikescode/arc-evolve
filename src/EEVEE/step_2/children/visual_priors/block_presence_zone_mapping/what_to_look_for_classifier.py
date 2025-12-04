CLASSIFIER_PROMPT = """Does this puzzle exhibit BLOCK PRESENCE MAPPING TO A FIXED-SIZE SUMMARY GRID?

This pattern means:
- The input contains multiple distinct 2x2 blocks of a non-background color scattered across the grid
- The output is always a fixed small grid (e.g., 3x3)
- The input grid is conceptually divided into regions/zones
- Each cell in the output corresponds to whether a 2x2 block exists in that region of the input
- Output uses a marker color (non-zero) to indicate presence, background (zero) for absence

Look at the training examples:
- Is the output always the same fixed size regardless of input size?
- Does the input contain multiple identical small blocks (like 2x2 squares)?
- Does the number/position of marked cells in output correlate with block positions in input?
- Are the blocks arranged in a grid-like pattern that maps to output cells?

Answer ONLY with: YES or NO"""
