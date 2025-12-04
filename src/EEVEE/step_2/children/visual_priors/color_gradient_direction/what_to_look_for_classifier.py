CLASSIFIER_PROMPT = """Does this puzzle involve DETECTING COLOR GRADIENT DIRECTION?

This pattern means:
- The input grid contains regions of different colors or a uniform color
- The output grid is the same size as the input
- The output marks a LINE (diagonal, anti-diagonal, or horizontal) with a marker color
- The rest of the output is filled with background color
- The line direction corresponds to how colors transition or are arranged in the input

Look at the training examples:
- Does the output always contain a single line of non-background cells?
- Is the line either: main diagonal, anti-diagonal, or horizontal?
- Does the direction of this line relate to how colors are distributed in the input?
- Are uniform inputs (all one color) treated as a special case?

Answer ONLY with: YES or NO"""
