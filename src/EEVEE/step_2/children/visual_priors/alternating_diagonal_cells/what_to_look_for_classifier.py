CLASSIFIER_PROMPT = """Does this puzzle exhibit ALTERNATING DIAGONAL CELLS transformation?

This pattern involves:
- Non-zero cells arranged along one or more diagonal lines
- Each diagonal line has cells that step diagonally (moving +1 row and +1 column, or similar)
- In the output, alternating cells along each diagonal are changed to a different color
- The pattern alternates: original color, new color, original color, new color, etc.
- The first and last cells of each diagonal segment typically remain the original color

Look at the training examples:
- Are the non-zero cells positioned along diagonal paths?
- Does the output show every other cell along each diagonal changed to a different color?
- Do the endpoints of diagonal segments retain their original color?
- Is there a consistent alternating pattern (keep, change, keep, change)?

Answer ONLY with: YES or NO"""
