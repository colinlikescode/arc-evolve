CLASSIFIER_PROMPT = """Does this puzzle involve PAIRING SAME-COLORED MARKERS TO FORM FILLED RECTANGLES?

Look for these indicators:
- The input contains sparse non-zero cells (markers) on a background of zeros
- Markers of the same color appear in pairs (exactly 2 cells of each color)
- In the output, each pair of same-colored markers defines the corners of a filled rectangle
- The rectangle is filled entirely with that color
- Different colored pairs create separate rectangles that don't interact

Check the training examples:
- Are there exactly 2 cells of each non-zero color in the input?
- Does each pair of same-colored cells become the opposite corners of a solid rectangle?
- Is the rectangle filled with the same color as the marker cells?

Answer ONLY with: YES or NO"""
