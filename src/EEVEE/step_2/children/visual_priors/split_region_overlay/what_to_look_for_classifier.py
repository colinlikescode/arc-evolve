CLASSIFIER_PROMPT = """Does this puzzle exhibit SPLIT REGION OVERLAY/MERGE pattern?

This pattern means:
- The input grid has a clear empty/zero region in the middle (vertical or horizontal strip)
- The input is divided into two separate regions (left and right, or top and bottom) by this empty strip
- These two regions contain the same non-zero color forming partial patterns
- The output is smaller than the input and represents the COMBINATION/OVERLAY of the two regions
- The output merges the non-zero cells from both regions into a single consolidated pattern

Look at the training examples:
- Is there a vertical or horizontal strip of zeros dividing the input into two parts?
- Do both parts contain scattered non-zero cells of the same color?
- Is the output approximately half the width (or height) of the input?
- Does the output appear to be a union/overlay of the patterns from both halves?

Answer ONLY with: YES or NO"""
