CLASSIFIER_PROMPT = """Does this puzzle involve FILLING THE LARGEST RECTANGULAR HOLE?

Look for these indicators:
- The input grid contains scattered non-zero values with some regions of contiguous background (zero) cells
- The output is nearly identical to the input, except one rectangular region of background cells is now filled with a new marker color
- The filled region appears to be the largest contiguous rectangular block of background cells in the grid
- Only ONE rectangular region gets filled, and it's filled uniformly with a single new color not present in the input

Check the training examples:
- Is there a rectangular area of background cells that becomes a solid block of a new color?
- Does the rest of the grid remain unchanged?
- Is the filled rectangle the largest such background rectangle in the grid?

Answer ONLY with: YES or NO"""
