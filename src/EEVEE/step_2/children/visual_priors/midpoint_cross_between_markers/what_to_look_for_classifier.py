CLASSIFIER_PROMPT = """Does this puzzle exhibit MIDPOINT MARKER BETWEEN PAIRED POINTS?

This pattern involves:
- The input contains exactly TWO non-zero marker cells of the same color
- These two markers define endpoints (either on the same row OR same column)
- The output adds a small cross/plus shape at the MIDPOINT between the two markers
- The cross shape uses a DIFFERENT color than the original markers
- The original markers remain unchanged in the output

Look at the training examples:
- Are there exactly two identical non-zero cells in the input?
- Are they aligned (same row or same column)?
- Does the output add a plus/cross shape centered between them?
- Is the cross made of a new color not present in the input?

Answer ONLY with: YES or NO"""
