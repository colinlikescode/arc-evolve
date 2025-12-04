CLASSIFIER_PROMPT = """Does this puzzle exhibit PATTERN COPYING TO A MARKER LOCATION?

This pattern involves:
- A small multi-colored pattern/shape somewhere in the grid
- A single isolated marker cell (distinct color) at a different location in the grid
- The transformation copies the pattern to the marker location, positioning the pattern relative to where the marker was
- The marker cell is replaced/removed and the pattern appears centered or anchored at that position
- The original pattern remains in place

Look at the training examples:
- Is there a cohesive multi-cell colored pattern in one area of the grid?
- Is there a single isolated cell of a different color elsewhere (acting as a marker)?
- In the output, does the pattern appear copied to where the marker was?
- Does the marker cell disappear, replaced by the copied pattern?
- Does the original pattern stay unchanged?

Answer ONLY with: YES or NO"""
