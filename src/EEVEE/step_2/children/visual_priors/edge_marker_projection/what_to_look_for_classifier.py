CLASSIFIER_PROMPT = """Does this puzzle exhibit EDGE MARKER PROJECTION onto a central rectangular block?

This pattern involves:
- A central rectangular block of uniform "fill" color (not background)
- Isolated single-cell "marker" pixels scattered around the edges of the grid (on the borders or aligned with the block's rows/columns)
- These markers are positioned either: above/below the block (aligned with columns), or left/right of the block (aligned with rows)

Look at the training examples:
- Is there a solid rectangular region of one color in the middle area?
- Are there isolated non-zero, non-block-colored pixels around the perimeter or edges?
- Do these edge markers appear to "project" or "extend" toward the central block?
- In the output, do the edge cells of the block get replaced with the colors of the corresponding markers?

Answer ONLY with: YES or NO"""
