CLASSIFIER_PROMPT = """Does this puzzle involve COUNTING NON-ZERO CELLS and producing a 1-ROW OUTPUT?

Look for these indicators:
- The input is a small grid containing scattered non-zero cells of a single color against a zero/black background
- The output is a single row (1×N grid)
- The output consists entirely of cells filled with the same non-zero color from the input
- The NUMBER of cells in the output row appears to equal the COUNT of non-zero cells in the input

Check the training examples:
- Does each input have exactly one non-zero color value (ignoring zeros)?
- Is the output always a 1-row grid?
- Does the width of the output equal the number of non-zero cells in the input?
- Is the output filled entirely with the non-zero color from the input?

Answer ONLY with: YES or NO"""
