CLASSIFIER_PROMPT = """Does this puzzle exhibit GRAVITY/DOWNWARD SHIFT of a pattern?

Gravity/downward shift means:
- The non-zero colored cells (the pattern) move downward by one row
- The pattern shape and colors are preserved exactly
- The top row becomes empty (filled with background/zero) after the shift
- The pattern "falls" toward the bottom of the grid

Look at the training examples:
- Does the colored pattern appear in the same position but shifted down by exactly one row?
- Is the top row of the output all zeros/background?
- Is the pattern shape and structure identical, just moved vertically?
- Does the bottom row of the input (if empty) now contain part of the pattern?

Answer ONLY with: YES or NO"""
