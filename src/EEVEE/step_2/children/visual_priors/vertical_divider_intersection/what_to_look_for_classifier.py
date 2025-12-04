CLASSIFIER_PROMPT = """Does this puzzle exhibit a VERTICAL DIVIDER COMPARISON pattern?

This pattern means:
- The input grid has a vertical divider (a column of a distinct separator color) that splits the grid into LEFT and RIGHT halves
- The output grid is the same size as ONE of the halves (not the full input)
- The output marks positions where a specific comparison between the left and right halves is TRUE
- Cells that satisfy the comparison condition are marked with a special output color
- Cells that don't satisfy the condition remain as background (zero)

Look at the training examples:
- Is there a single column of a unique color dividing the input into two equal-width regions?
- Is the output width equal to the width of one half (not including the divider)?
- Does the output appear to show results of comparing corresponding cells from left and right halves?
- Are marked cells in the output at positions where both halves had the same non-zero value, or where they differed?

Answer ONLY with: YES or NO"""
