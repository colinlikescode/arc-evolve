CLASSIFIER_PROMPT = """Does this puzzle involve QUADRANT OVERLAY/MERGING?

Look for these indicators:
- The input grid is divided into 4 quadrants by separator lines (a row and column of a single color running through the middle)
- Each quadrant contains a distinct pattern with its own dominant non-zero color
- The output is the same size as one quadrant
- The output appears to combine or merge information from multiple quadrants

Check if:
- There's a clear cross-shaped separator dividing the grid into 4 equal regions
- Each region has a different primary color
- The output dimensions match the quadrant dimensions
- The output contains colors from multiple quadrants merged together

Answer ONLY with: YES or NO"""
