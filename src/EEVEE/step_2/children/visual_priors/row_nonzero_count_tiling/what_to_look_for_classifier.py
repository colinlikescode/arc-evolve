CLASSIFIER_PROMPT = """Does this puzzle exhibit ROW-BASED TILING WITH NON-ZERO ROW COUNTING?

This pattern means:
- The input is a small grid (e.g., 3x3)
- The output is a larger grid where the dimensions depend on counting non-zero cells
- Count the number of non-zero cells in EACH ROW of the input
- For each row, tile/repeat the input pattern horizontally that many times
- The output width = input_width × maximum_non_zero_count_per_row
- The output height = input_height × number_of_rows_with_at_least_one_non_zero_cell
- Rows with non-zero cells get the input pattern tiled; remaining rows are filled with zeros

Look at the training examples:
- Is the output significantly larger than the input?
- Does the pattern appear to be horizontally tiled in certain rows?
- Does the number of horizontal repetitions vary by row based on non-zero cell counts?
- Are there large regions of zeros filling out the grid?

Answer ONLY with: YES or NO"""
