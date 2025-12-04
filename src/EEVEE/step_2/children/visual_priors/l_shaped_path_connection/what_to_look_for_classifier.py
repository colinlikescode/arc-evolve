CLASSIFIER_PROMPT = """Does this puzzle exhibit an L-SHAPED PATH CONNECTING TWO MARKER POINTS?

L-shaped path connection means:
- The input contains exactly TWO distinct non-zero colored marker cells on a background of zeros
- These two markers are at different row AND column positions (not aligned)
- The output draws an L-shaped path connecting these two markers
- The path consists of a vertical segment and a horizontal segment that meet at a corner
- The path is drawn using a THIRD color (different from both markers)
- Both original markers remain in place in the output

Look at the training examples:
- Are there exactly two isolated non-zero cells in the input?
- Do these two cells have different colors from each other?
- Does the output show an L-shaped line connecting them?
- Is the connecting line drawn in a new color not present in the input?
- Does the path go vertically from one marker and horizontally from the other, meeting at the corner?

Answer ONLY with: YES or NO"""
