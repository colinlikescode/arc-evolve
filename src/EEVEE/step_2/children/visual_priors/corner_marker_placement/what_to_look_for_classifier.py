CLASSIFIER_PROMPT = """Does this puzzle involve CORNER MARKER PLACEMENT around rectangular blocks?

Look for these indicators:
- The input contains one or more rectangular blocks of a uniform non-background color (typically 2x2 or similar small blocks)
- The output preserves these blocks in their original positions
- The output adds four distinct colored markers at the CORNERS around each block
- The markers are placed diagonally adjacent to the block corners (one cell away from each corner)
- Each corner position uses a different color marker (e.g., top-left, top-right, bottom-left, bottom-right each get a unique color)
- The same four marker colors are used consistently for all blocks in the grid

Check the training examples:
- Are there small rectangular blocks of a single color in the input?
- Does the output add exactly 4 new colored cells around each block?
- Are these new cells positioned at diagonal corners relative to the block?
- Do the corner markers follow a consistent pattern (same color for same relative corner position)?

Answer ONLY with: YES or NO"""
