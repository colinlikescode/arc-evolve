CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A SUBREGION from a larger grid?

Look for these indicators:
- The input is a larger grid that can be evenly divided into smaller blocks
- The output is exactly the size of one of these blocks
- The output appears to be a direct copy of one specific region from the input
- The grid dimensions suggest a natural subdivision (e.g., 9x9 → 3x3 blocks, 6x6 → 2x2 or 3x3 blocks)

Check if:
- The input dimensions are multiples of the output dimensions
- The output matches exactly one rectangular region of the input
- The same relative position is used across all training examples

Answer ONLY with: YES or NO"""
