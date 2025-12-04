CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER-MARKER EXTRACTION WITH COLOR REPLACEMENT?

This pattern involves:
- Four corner markers (same color) forming a rectangular boundary in the input
- A pattern/shape made of a different color located INSIDE this rectangular region
- The output extracts ONLY the region bounded by the corner markers
- The pattern color is REPLACED with the corner marker color in the output

Look at the training examples:
- Are there exactly 4 cells of one color forming corners of a rectangle?
- Is there a distinct pattern/shape made of a different color inside that rectangle?
- Is the output a smaller grid containing just the bounded region?
- Does the output show the same pattern shape but colored with the corner marker color?

Answer ONLY with: YES or NO"""
