CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING ORIENTED PATTERNS AND ASSEMBLING INTO A GRID?

Look for these indicators:
- The input is a larger grid containing multiple small patterns (same size) scattered at various positions
- Each small pattern has a consistent base/neutral color with a distinct accent color forming a directional shape (corner, L-shape, or edge cluster)
- The accent colors point or cluster toward a specific direction within each pattern (e.g., top-left corner, bottom-right corner, etc.)
- The output is a grid composed of these patterns arranged in a specific layout
- The output size is a multiple of the individual pattern size (e.g., 9x9 for 3x3 patterns arranged in 3x3)
- Each pattern's position in the output corresponds to its directional orientation

Answer ONLY with: YES or NO"""
