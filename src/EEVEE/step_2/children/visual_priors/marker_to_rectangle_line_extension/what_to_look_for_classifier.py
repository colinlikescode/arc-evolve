CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-TO-RECTANGLE LINE DRAWING?

This pattern means:
- There is a solid rectangular region of one distinct color (not the background)
- There are scattered single-cell "marker" pixels of another distinct color (not the background, not the rectangle color)
- The markers are positioned outside the rectangle
- In the output, lines are drawn FROM the rectangle edge TO certain markers

Look at the training examples:
- Is there a rectangular block of uniform non-background color?
- Are there isolated single pixels of a different non-background color scattered around?
- Do lines appear in the output connecting the rectangle to some of these markers?
- Do the lines extend horizontally or vertically from the rectangle's edges toward markers that are aligned with the rectangle (same row or column)?

Answer ONLY with: YES or NO"""
