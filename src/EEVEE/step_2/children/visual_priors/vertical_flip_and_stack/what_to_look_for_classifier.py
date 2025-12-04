CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL FLIP AND STACK?

This pattern means:
- The output height is exactly double the input height
- The output width equals the input width
- The output consists of two copies of the input stacked vertically
- The TOP half of the output is the input with rows in REVERSED order (vertically flipped)
- The BOTTOM half of the output is the original input (or vice versa)
- Together, this creates a vertically symmetric result

Look at the training examples:
- Is the output exactly twice as tall as the input?
- Does the output have vertical mirror symmetry?
- Is the top half a vertical flip of the bottom half?
- Are both halves derived from the original input (one flipped, one not)?

Answer ONLY with: YES or NO"""
