CLASSIFIER_PROMPT = """Does this puzzle exhibit SCALED BLOCK EXPANSION based on non-zero cell count?

Scaled block expansion means:
- The input is a small grid (e.g., 3x3)
- The output is larger, with each input cell expanded into a square block
- The SCALE FACTOR equals the COUNT of non-zero cells in the input
- Each cell in the input becomes an N×N block in the output (where N = number of non-zero cells)
- Non-zero cells become N×N blocks filled with their color
- Zero cells become N×N blocks of zeros (background)

Look at the training examples:
- Count the non-zero cells in the input
- Is the output exactly (input_height × count) by (input_width × count)?
- Does each input cell expand into a block of size count × count?
- Are non-zero values replicated to fill their expanded blocks?

Answer ONLY with: YES or NO"""
