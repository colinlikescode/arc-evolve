CLASSIFIER_PROMPT = """Does this puzzle exhibit BORDER EXTENSION WITH CORNER ZEROING?

This pattern means:
- The output is larger than the input by exactly 2 in each dimension (H+2 × W+2)
- The original input appears in the center of the output
- Each row of the input is extended by duplicating the leftmost cell to the left and the rightmost cell to the right
- A top row is added (copy of first input row, extended similarly)
- A bottom row is added (copy of last input row, extended similarly)
- The four corner cells of the output are set to zero/background

Look at the training examples:
- Is the output exactly 2 rows taller and 2 columns wider than the input?
- Does the input content appear in the middle rows/columns?
- Are the edge cells duplicated outward along each row?
- Are all four corners of the output filled with zeros?

Answer ONLY with: YES or NO"""
