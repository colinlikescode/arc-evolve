CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL REFLECTION WITH VERTICAL TILING?

This pattern means:
- The input is a small rectangular grid (typically more rows than columns)
- The output width is exactly 2× the input width
- The output height is exactly input_height × input_height (squared)
- Each row in the output is formed by horizontally mirroring the corresponding input row (reversed + original)
- The resulting pattern is vertically repeated/tiled multiple times

Look at the training examples:
- Is the output width double the input width?
- Is the output height equal to input_height squared?
- Does each output row appear to be a horizontally symmetric version of the input row?
- Is there a repeating vertical pattern in the output?

Answer ONLY with: YES or NO"""
