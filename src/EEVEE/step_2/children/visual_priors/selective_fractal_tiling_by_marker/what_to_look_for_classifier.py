CLASSIFIER_PROMPT = """Does this puzzle exhibit SELECTIVE FRACTAL TILING based on a marker color?

Selective fractal tiling means:
- The input is a small grid (e.g., N×N)
- The output is N times larger in each dimension (N×N blocks, each block is N×N)
- One specific non-zero color acts as a "marker" or "placement indicator"
- For each cell containing the marker color in the input: place a copy of the ENTIRE input pattern in the corresponding block of the output
- All other blocks (where the marker color was NOT present) are filled with zeros/background

Look at the training examples:
- Is the output exactly N times larger than the input in each dimension?
- Does one particular non-zero color seem to determine WHERE the input pattern gets copied?
- Are there multiple copies of the input pattern placed in specific block positions?
- Do the block positions with the pattern correspond to where a specific color appeared in the input?

Answer ONLY with: YES or NO"""
