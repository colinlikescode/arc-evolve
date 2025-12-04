CLASSIFIER_PROMPT = """Does this puzzle involve PERPENDICULAR STRIPE INTERSECTION PRIORITY?

Look for these indicators:
- There is a vertical stripe (column or columns) of one non-background color running through the grid
- There is a horizontal stripe (row or rows) of a different non-background color running through the grid
- These two stripes intersect at certain cells
- At the intersection in the input, one stripe's color appears (blocking the other)
- The transformation involves changing which color appears at the intersection

Check the training examples:
- Are there exactly two non-background colors forming perpendicular lines?
- Does one line span vertically and one horizontally?
- Does the output differ from the input only at the intersection cells?

Answer ONLY with: YES or NO"""
