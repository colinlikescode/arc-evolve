CLASSIFIER_PROMPT = """Does this puzzle exhibit LINE FILL BETWEEN ENDPOINT PAIRS?

This pattern means:
- The input has pairs of non-zero colored cells on the same row (or column)
- One cell is at the left edge, another at the right edge of that row (or top/bottom for columns)
- The cells between them are all zeros/background
- The output fills the entire row between these endpoint pairs
- Each endpoint's color expands toward the center
- A special marker color appears at the meeting point in the middle

Look at the training examples:
- Are there exactly two non-zero cells on certain rows, positioned at opposite edges?
- Does the output show those colors expanded horizontally to meet in the middle?
- Is there a consistent "separator" or "meeting point" color where the two expansions meet?
- Do rows without endpoint pairs remain unchanged (all zeros)?

Answer ONLY with: YES or NO"""
