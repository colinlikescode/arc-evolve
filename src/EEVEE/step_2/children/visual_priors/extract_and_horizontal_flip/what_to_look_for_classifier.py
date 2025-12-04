CLASSIFIER_PROMPT = """Does this puzzle exhibit EXTRACT AND HORIZONTALLY FLIP pattern?

This pattern means:
- The input contains a rectangular region of non-background (non-zero) cells embedded within a larger grid of background (zero) cells
- The output is this non-background rectangular region EXTRACTED from the input
- The extracted region is then HORIZONTALLY FLIPPED (mirrored left-to-right)

Look at the training examples:
- Is there a single contiguous rectangular block of non-zero cells surrounded by zeros?
- Is the output smaller than the input (just the extracted region)?
- Does the output appear to be the horizontal mirror/flip of the non-zero region from the input?
- Are the same colors present in both input and output, just rearranged horizontally?

Answer ONLY with: YES or NO"""
