CLASSIFIER_PROMPT = """Does this puzzle involve CONNECTING PAIRS OF SAME-COLORED CELLS WITH DIAGONAL LINES?

Look for these indicators:
- The input contains scattered non-zero colored cells on a background
- Each distinct non-zero color appears exactly twice in the input
- The output shows diagonal lines connecting each pair of same-colored cells
- The diagonal lines are drawn using the same color as the endpoint cells
- Lines go from one cell to another moving diagonally (one step in row and one step in column per cell)

Check the training examples:
- Are there pairs of cells with matching colors?
- In the output, are those pairs connected by diagonal paths?
- Does each diagonal line use the color of its endpoint cells?

Answer ONLY with: YES or NO"""
