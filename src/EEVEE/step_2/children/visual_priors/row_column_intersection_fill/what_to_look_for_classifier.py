CLASSIFIER_PROMPT = """Does this puzzle exhibit ROW-COLUMN INTERSECTION FILLING?

This pattern involves:
- A row of marker cells (typically the first row) with non-zero values at certain column positions
- A column of marker cells (typically the last column) with non-zero values at certain row positions
- The transformation fills cells at the INTERSECTIONS of marked columns and marked rows with a new color
- The original marker cells are preserved
- Only interior intersection cells (not the original markers) receive the fill color

Look at the training examples:
- Is there a pattern of markers along one edge (e.g., top row)?
- Is there a pattern of markers along a perpendicular edge (e.g., right column)?
- Do new colored cells appear where the marked columns intersect with marked rows?
- Are the original marker positions preserved while intersections get a different color?

Answer ONLY with: YES or NO"""
