CLASSIFIER_PROMPT = """Does this puzzle involve NOISE REMOVAL FROM RECTANGULAR REGIONS?

Look for these indicators:
- The input contains one or more solid rectangular regions filled with a non-background color
- There are scattered isolated cells (noise) of the same color appearing OUTSIDE these rectangles
- Some rectangles may have "extra" cells extending beyond their clean rectangular boundary
- The output preserves the clean rectangular regions but removes all isolated scattered cells
- Rectangles in the output have clean, consistent boundaries (no protruding cells)

Key pattern:
- Solid filled rectangles = KEEP (but clean up any boundary irregularities)
- Isolated single cells or small scattered pixels = REMOVE (these are noise)
- The transformation distinguishes between structured rectangular shapes and random noise

Answer ONLY with: YES or NO"""
