CLASSIFIER_PROMPT = """Does this puzzle involve COUNTING MARKERS AND DISPLAYING AS A BAR/TALLY?

This pattern means:
- The input contains scattered marker cells (non-background color) at various positions
- The output represents the COUNT of those markers as a horizontal bar
- The bar starts at the top-left corner and extends rightward
- If the count exceeds the width, additional markers appear in a specific overflow pattern (typically centered in the next row)
- The marker color changes from input to output (but the count is preserved)

Look at the training examples:
- Are there scattered non-zero cells in the input?
- Does the output show a consolidated horizontal line of cells starting from top-left?
- Does the number of output colored cells equal the count of input colored cells?
- Is the output pattern independent of WHERE the input markers were located?

Answer ONLY with: YES or NO"""
