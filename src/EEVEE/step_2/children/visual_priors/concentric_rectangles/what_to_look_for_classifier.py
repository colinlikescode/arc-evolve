CLASSIFIER_PROMPT = """Does this puzzle exhibit a SPIRAL PATTERN emanating from a CROSS/PLUS shape?

This pattern means:
- The input contains a CROSS or PLUS shape made of colored cells
- The cross has a CENTER that is EMPTY (background) with arms extending in 4 directions
- The output creates a SPIRAL pattern that emanates outward from the cross center
- The spiral winds around the grid, creating alternating filled and empty paths
- The spiral continues until it reaches the edges of the grid

Look at the training examples:
- Does the input have a small CROSS/PLUS shape with an empty center?
- Does the output show a SPIRAL pattern winding outward from where the cross was?
- Are there alternating bands of colored and empty cells forming the spiral?
- Does the spiral extend to fill most of the grid?

Answer ONLY with: YES or NO"""
