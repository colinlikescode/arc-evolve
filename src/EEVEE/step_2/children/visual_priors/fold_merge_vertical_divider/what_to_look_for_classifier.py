CLASSIFIER_PROMPT = """Does this puzzle involve MERGING TWO HALVES ACROSS A VERTICAL DIVIDER?

Look for these indicators:
- The input has a vertical line/column of a single color running from top to bottom that divides the grid
- This dividing column acts as a "fold line" or separator
- The left and right portions of the grid contain scattered non-zero colored cells
- The output is approximately half the width of the input (minus the divider)
- The output appears to combine or overlay content from both sides

Key structural features:
- A consistent vertical separator column (same color throughout)
- Non-zero cells on both sides of the separator
- Output height equals input height
- Output width is roughly half the input width

Answer ONLY with: YES or NO"""
