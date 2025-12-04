CLASSIFIER_PROMPT = """Does this puzzle exhibit NESTED RECTANGULAR SPIRALS FROM POINT MARKERS?

This pattern involves:
- The input is mostly empty (background color) with a small number of scattered single-cell markers (all same non-background color)
- The markers form a diagonal or staircase pattern across the grid
- The output draws nested rectangular frames/spirals using the marker color
- Each marker defines a "corner" or "turning point" for one of the nested rectangles
- The rectangles are concentric, expanding outward from the innermost marker
- The spacing between rectangles corresponds to the spacing between the original markers

Look at the training examples:
- Are there just a few isolated single-cell markers of the same color on an empty background?
- Do the markers appear to form a diagonal line or staircase pattern?
- Does the output show nested rectangular outlines that pass through or near the marker positions?
- Do the rectangles expand outward with consistent spacing related to marker distances?

Answer ONLY with: YES or NO"""
