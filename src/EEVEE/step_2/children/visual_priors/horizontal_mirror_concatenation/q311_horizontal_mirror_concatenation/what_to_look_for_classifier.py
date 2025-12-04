CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL CONCATENATION WITH REFLECTION?

This pattern means:
- The output width is exactly 2× the input width
- The output height equals the input height
- The output consists of the original input placed side-by-side with a horizontally reflected (mirrored) version of itself
- The reflection is along the vertical axis (left-right flip)

Look at the training examples:
- Is the output exactly twice as wide as the input?
- Does the left half of the output match the input?
- Does the right half of the output appear to be a horizontal mirror of the input?
- Are the non-zero cells in the output symmetric around the vertical center line?

Answer ONLY with: YES or NO"""
