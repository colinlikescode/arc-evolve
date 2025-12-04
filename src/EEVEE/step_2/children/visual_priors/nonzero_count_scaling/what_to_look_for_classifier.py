CLASSIFIER_PROMPT = """Does this puzzle exhibit CELL-WISE SCALING WITH VARIABLE SCALE FACTOR?

This pattern means:
- The input is a small grid (typically 3x3 or similar)
- The output is a scaled-up version where each input cell becomes a square block
- The scale factor is determined by counting NON-ZERO cells in the input
- Each cell in the input becomes an N×N block in the output (where N = count of non-zero cells)
- The color of each block matches the corresponding input cell's color
- Zero cells become blocks of zeros, non-zero cells become blocks of that color

Look at the training examples:
- Is the output size equal to input_size × (number of non-zero cells in input)?
- Does each input cell expand into a uniform square block?
- Is the scale factor consistent with the count of non-zero values?
- Are the relative positions preserved (just scaled up)?

Answer ONLY with: YES or NO"""
