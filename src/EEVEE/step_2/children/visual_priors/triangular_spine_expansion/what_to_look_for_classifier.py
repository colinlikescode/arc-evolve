CLASSIFIER_PROMPT = """Does this puzzle exhibit a TRIANGULAR EXPANSION FROM A VERTICAL LINE?

This pattern involves:
- The input has a single vertical line of non-zero colored cells (a "spine")
- The output creates a triangular/diagonal expansion pattern emanating from this spine
- The triangle grows outward from the spine, with alternating colors creating a checkerboard-like pattern
- The expansion is bounded by the length of the vertical line (rows where the line exists)
- The triangle tapers as it approaches the bottom of the original line

Look at the training examples:
- Is there a single vertical column of identical non-zero values in the input?
- Does the output show a triangular region filled with alternating colors?
- Does the triangle expand from the top of the line and narrow toward the bottom?
- Is there a secondary color introduced that alternates with the original line color?

Answer ONLY with: YES or NO"""
