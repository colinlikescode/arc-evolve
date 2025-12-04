CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL TILING / REPEATING PATTERN EXTRACTION?

Horizontal tiling means:
- The input grid contains a pattern that repeats horizontally (left to right)
- The same tile/block is repeated N times across the width
- The output is the single repeating unit (the base tile)
- The input width is a multiple of the output width
- The input height equals the output height

Look at the training examples:
- Is the input wider than it is tall (or at least wider than the output)?
- Can you identify a repeating pattern when scanning from left to right?
- Does the input width appear to be 2x, 3x, or more times some base width?
- Is the output a single instance of the repeating unit?

Answer ONLY with: YES or NO"""
