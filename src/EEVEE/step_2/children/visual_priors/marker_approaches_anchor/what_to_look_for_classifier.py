CLASSIFIER_PROMPT = """Does this puzzle involve TWO MARKERS MOVING TOWARD EACH OTHER (or one toward a fixed anchor)?

Look for these indicators:
- The input contains exactly TWO non-zero colored cells on a background of zeros
- One of the colored cells moves closer to the other in the output
- The other colored cell either stays fixed OR also moves toward the first
- Movement is by exactly one cell along the direction connecting the two markers
- The grid size remains the same between input and output

Check if:
- Are there exactly two distinct non-zero cells in the input?
- Does one (or both) of them shift position by one cell toward the other?
- Is the rest of the grid unchanged (all zeros remain zeros)?

Answer ONLY with: YES or NO"""
