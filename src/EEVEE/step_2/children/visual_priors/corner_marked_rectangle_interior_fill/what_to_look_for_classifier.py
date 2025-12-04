CLASSIFIER_PROMPT = """Does this puzzle involve FILLING THE INTERIOR OF RECTANGULAR REGIONS DEFINED BY CORNER MARKERS?

Look for these indicators:
- Are there exactly 4 cells of a non-background color forming the corners of a rectangle?
- Are there potentially multiple such rectangular regions defined by corner markers?
- In the output, is the interior region between the corner markers filled with a different color?
- Do the corner markers remain in place while only the interior gets filled?

The pattern involves:
- Groups of 4 marker cells that define rectangular boundaries (corners)
- The rectangular interior (excluding the corners and edges) gets filled with a secondary color
- Multiple independent rectangles may exist in the same grid

Answer ONLY with: YES or NO"""
