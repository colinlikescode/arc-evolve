CLASSIFIER_PROMPT = """Does this puzzle exhibit UNIFORM 2x2 CELL SCALING?

Uniform 2x2 cell scaling means:
- The output grid is exactly 2 times larger than the input in BOTH dimensions
- Each individual cell from the input becomes a 2x2 block of the same color in the output
- The transformation is a simple pixel-doubling or nearest-neighbor upscaling
- Every cell is scaled identically - no special treatment for any color

Look at the training examples:
- Is the output exactly twice the height and twice the width of the input?
- Does each cell in the input correspond to a 2x2 block of identical color in the output?
- Is this a straightforward scaling operation with no other transformations?
- Are all colors (including the background/zero color) scaled the same way?

Answer ONLY with: YES or NO"""
