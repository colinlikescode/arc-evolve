CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER EXPANSION WITH CROSS PATTERN?

This pattern means:
- The input contains sparse marker cells (non-zero, non-background) scattered on a background
- Each marker cell gets expanded into a small fixed pattern (like a cross or plus shape) centered on or near the marker
- The expansion pattern uses the original marker color AND introduces a secondary color
- The secondary color appears in the cardinal directions (up, down, left, right) from the marker
- The original marker color appears at the diagonal corners of the expansion

Look at the training examples:
- Are there isolated single cells of a non-background color in the input?
- Does each marker become a 3x3 cross-like pattern in the output?
- Is there a new color introduced that wasn't in the input (appearing in the cross arms)?
- Does the original marker color appear at the four corners of each 3x3 expansion?
- Is the center of each 3x3 pattern the background color (creating a hollow cross)?

Answer ONLY with: YES or NO"""
