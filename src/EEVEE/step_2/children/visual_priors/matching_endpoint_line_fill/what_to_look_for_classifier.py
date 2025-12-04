CLASSIFIER_PROMPT = """Does this puzzle exhibit MATCHING ENDPOINT LINE FILL?

This pattern involves:
- A grid where certain rows have non-zero colored cells at the leftmost and rightmost positions only
- The interior cells between these endpoints are initially empty (zeros/background)
- The transformation rule: if the left endpoint and right endpoint of a row have the SAME color value, fill the entire row with that color
- If the endpoints have DIFFERENT colors, leave the row unchanged

Look at the training examples:
- Are there rows with colored cells only at the left and right edges?
- Do rows where both edge colors match get filled horizontally with that color?
- Do rows where edge colors differ remain unchanged (just the two endpoints)?

Answer ONLY with: YES or NO"""
