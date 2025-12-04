CLASSIFIER_PROMPT = """Does this puzzle involve COMPLETING L-SHAPES WITH A CORNER MARKER?

This pattern means:
- The input contains one or more L-shaped patterns (3 connected cells forming an "L")
- Each L-shape is made of a single non-zero/non-background color
- The L-shapes can be in any of 4 orientations (rotations)
- In the output, a marker of a different color is placed at the "missing corner" - the position that would complete each L into a 2x2 square

Look at the training examples:
- Are there small L-shaped clusters of 3 cells each?
- Does the output add a single cell of a new color adjacent to each L-shape?
- Is the new cell placed where a 2x2 square would be completed?

Answer ONLY with: YES or NO"""
