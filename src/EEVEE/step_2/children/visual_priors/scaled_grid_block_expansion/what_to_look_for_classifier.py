CLASSIFIER_PROMPT = """Does this puzzle exhibit SCALED GRID EXPANSION WITH BLOCK PLACEMENT?

This pattern means:
- The input is a sparse grid with isolated non-zero cells scattered at various positions
- The output is exactly 2x the size of the input in both dimensions
- Each non-zero cell in the input becomes a filled square block in the output
- The block size is typically a fixed small size (like 4x4)
- The position of each block in the output corresponds to the scaled position of the original cell
- Specifically: a cell at position (row, col) in the input maps to a block starting at position (row*2, col*2) in the output
- Multiple non-zero cells on the same row in the input create adjacent or separated blocks on the same row band in the output

Look at the training examples:
- Is the output grid exactly twice the dimensions of the input?
- Are there sparse isolated colored cells in the input?
- Does each colored cell become a small filled square block in the output?
- Do the blocks appear at positions that are scaled versions of the original cell positions?

Answer ONLY with: YES or NO"""
