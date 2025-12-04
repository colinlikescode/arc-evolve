CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING ONE REGION FROM MULTIPLE CANDIDATE REGIONS?

Look for these indicators:
- The input is a larger grid containing multiple distinct rectangular regions of the same size
- These regions are separated by background (zero) cells
- Each region contains patterns made of non-zero values
- The output is a single region matching the size of the candidate regions
- The output appears to be one specific region selected from the input based on some criterion (e.g., most instances of a particular color, most diverse, unique pattern)

Check if:
- Multiple similarly-sized non-overlapping pattern blocks exist in the input
- The blocks contain varying amounts of different non-zero colors
- The output matches exactly one of these blocks
- The selected block appears to be the one with the most instances of a secondary/accent color

Answer ONLY with: YES or NO"""
