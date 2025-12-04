CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING THE CENTER COLUMN?

Center column extraction means:
- The output grid has the same dimensions as the input grid
- Only the middle/center column from the input is preserved in the output
- All other cells (non-center columns) are set to the background color (zero)
- The center column values remain in their original positions

Look at the training examples:
- Is the output mostly zeros/background except for one vertical column?
- Is the preserved column in the center (middle) position of the grid?
- Do the values in that center column match exactly between input and output?
- Are all other columns completely zeroed out?

Answer ONLY with: YES or NO"""
