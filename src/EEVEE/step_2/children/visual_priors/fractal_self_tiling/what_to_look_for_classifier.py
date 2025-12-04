CLASSIFIER_PROMPT = """Does this puzzle exhibit SELF-SIMILAR FRACTAL TILING?

Self-similar fractal tiling means:
- The input is a small grid (e.g., 3x3)
- The output is a larger grid that is N times bigger in each dimension (e.g., 9x9 for 3x scale)
- The output is divided into blocks, where each block corresponds to a cell in the input
- For each NON-ZERO cell in the input: place a copy of the ENTIRE input pattern in that block
- For each ZERO cell in the input: place a block of all zeros (background)

This creates a fractal/self-similar pattern where the input pattern references itself.

Look at the training examples:
- Is the output exactly N times larger than the input in each dimension?
- Does the output look like a tiled version of the input?
- Do non-zero cells in the input correspond to copies of the full pattern in the output?
- Do zero/background cells in the input correspond to all-zero blocks in the output?

Answer ONLY with: YES or NO"""
