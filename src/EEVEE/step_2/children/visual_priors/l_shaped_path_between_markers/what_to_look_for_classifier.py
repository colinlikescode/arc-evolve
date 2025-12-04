CLASSIFIER_PROMPT = """Does this puzzle exhibit an L-SHAPED PATH CONNECTING TWO MARKER POINTS?

Look for these characteristics:
- The input contains exactly TWO distinct non-zero colored cells (marker points) on a background of zeros
- These two markers are at different row AND column positions (not aligned horizontally or vertically)
- The output draws an L-shaped (right-angle) path connecting these two markers
- The path uses a NEW color (not present in the input) as a connector/fill color
- The path goes horizontally from one marker then vertically to the other (or vice versa), forming a right angle
- The original marker colors are preserved at their positions

Look at the training examples:
- Are there exactly two isolated non-zero cells in the input?
- Does the output show an L-shaped line connecting them?
- Is a third color introduced to draw the connecting path?
- Does the path form a corner at the intersection of the row of one marker and column of the other?

Answer ONLY with: YES or NO"""
