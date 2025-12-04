CLASSIFIER_PROMPT = """Does this puzzle involve COUNTING AND RANKING MINORITY COLORS IN A BLOCK GRID?

Look for these indicators:
- The input is a grid containing regularly spaced small blocks (e.g., 2x2) separated by a background color (typically zeros)
- One color appears in most of the blocks (the "dominant" or "majority" color)
- Several other colors appear in fewer blocks (the "minority" colors)
- The output is a small column (Nx1) listing colors
- The output appears to list the minority colors ranked by their frequency

Key questions:
- Is there a clear grid structure of repeated small blocks?
- Is one block color significantly more common than others?
- Does the output size correspond to the number of distinct minority colors?

Answer ONLY with: YES or NO"""
