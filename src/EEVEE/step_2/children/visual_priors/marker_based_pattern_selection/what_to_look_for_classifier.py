CLASSIFIER_PROMPT = """Does this puzzle involve PATTERN SELECTION based on a MARKER CELL?

Look for these indicators:
- The input contains multiple distinct colored regions/shapes scattered across the grid
- One of the regions contains a special MARKER cell (a unique color that appears only once, typically at the center of one shape)
- The output is a small grid (often 3x3) that represents ONE of the input shapes
- The selected shape is the one containing the marker cell, but the marker is replaced with the shape's own color

Check:
- Are there multiple separate colored patterns in the input?
- Is there exactly one cell with a unique "marker" color that doesn't match any of the pattern colors?
- Does the output match the shape of the pattern that contains this marker?
- Is the marker cell replaced with the surrounding pattern's color in the output?

Answer ONLY with: YES or NO"""
