CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-GUIDED LINE EXTENSION/PROJECTION?

This pattern involves:
- A row or column containing a pattern of marked cells (one distinct color)
- A perpendicular row or column containing marker cells (a different distinct color)
- The marked pattern gets "projected" or extended across the grid
- Each marker indicates a shift/offset point where the pattern changes position

Look at the training examples:
- Is there a line (row or column) with a repeating pattern of non-background cells?
- Is there a perpendicular line with marker cells of a different color?
- Does the pattern appear to shift/slide at each marker position?
- Do the markers remain in place while the pattern extends through the grid?

Answer ONLY with: YES or NO"""
