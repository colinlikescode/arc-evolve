CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL GAP FILLING BETWEEN MARKERS?

This pattern means:
- The input contains pairs (or sequences) of identical non-zero marker cells on the same row
- These markers are separated by background cells (gaps)
- The transformation fills the gaps between consecutive markers with a secondary color
- The original markers remain in place

Look at the training examples:
- Are there rows with two or more identical non-zero cells separated by gaps?
- Do the gaps between these same-row markers get filled with a different color in the output?
- Does the filling create a connected horizontal line segment between markers?
- Do the original marker cells remain unchanged?

Answer ONLY with: YES or NO"""
