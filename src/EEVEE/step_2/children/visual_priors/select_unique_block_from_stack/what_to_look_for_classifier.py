CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING ONE BLOCK from a vertically stacked grid of equal-sized blocks?

Look for these indicators:
- The input is a tall grid that can be evenly divided into N equal horizontal blocks (e.g., 9 rows → three 3-row blocks)
- The output is exactly one of these blocks (same width, height = input_height / N)
- Each block contains a different two-color pattern
- The selection criteria appears to be based on which block has the most unique/asymmetric internal pattern (where one color dominates and another appears in a distinctive non-symmetric arrangement)

Check if:
- Input height is a multiple of output height
- Output matches exactly one horizontal section of the input
- The selected block has a pattern where colors are distributed asymmetrically

Answer ONLY with: YES or NO"""
