CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING AND ASSEMBLING SCATTERED L-SHAPED PATTERNS?

This pattern type means:
- The input contains multiple small L-shaped or corner patterns (each typically 3 cells forming an L in a 2x2 area)
- Each pattern is a different color and located in a different region of the grid
- The patterns are scattered across roughly 4 quadrants of the input
- The output is a smaller grid that assembles all patterns together
- Each pattern is placed in the output quadrant corresponding to its relative position in the input
- The patterns are arranged so they point toward the center, creating a composite shape

Look at the training examples:
- Are there exactly 4 small L-shaped patterns of different colors?
- Is each pattern located in a different quadrant of the input?
- Does the output combine these patterns into a 4x4 grid with each pattern in its corresponding quadrant?

Answer ONLY with: YES or NO"""
