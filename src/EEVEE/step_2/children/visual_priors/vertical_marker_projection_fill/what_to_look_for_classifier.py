CLASSIFIER_PROMPT = """Does this puzzle involve VERTICAL PROJECTION OF MARKERS TO FILL HOLES IN A SHAPE?

Look for these indicators:
- There is a contiguous shape made of one non-background color in one region of the grid (often upper portion)
- The shape contains some holes (background-colored cells within it)
- There are isolated marker cells of a different non-background color in another region (often lower portion)
- These markers appear to form vertical lines or columns
- In the output, the markers have "moved" to fill holes in the shape that align vertically with the marker columns
- The original marker positions (outside the shape) become background color

The transformation projects markers vertically into holes within a shape.

Answer ONLY with: YES or NO"""
