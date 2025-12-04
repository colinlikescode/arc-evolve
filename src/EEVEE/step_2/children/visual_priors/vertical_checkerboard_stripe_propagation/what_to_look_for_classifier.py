CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL STRIPE PROPAGATION with alternating checkerboard pattern?

This pattern means:
- The input has one or more non-zero "seed" cells in the FIRST ROW only
- The rest of the grid is filled with zeros (background)
- Each seed cell generates a vertical stripe pattern that extends downward through all rows
- The stripe pattern alternates in a checkerboard fashion: on odd rows, the color appears at the seed position; on even rows, the color appears at positions one to the left AND one to the right of the seed

Look at the training examples:
- Are there colored cells only in the top row of the input?
- Is the rest of the input grid entirely zeros?
- Does each colored cell in the top row create a vertical "zigzag" or checkerboard stripe pattern in the output?
- Does the pattern alternate: center on odd rows, left+right on even rows?

Answer ONLY with: YES or NO"""
