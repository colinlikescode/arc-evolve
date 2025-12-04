CLASSIFIER_PROMPT = """Does this puzzle exhibit ROW/COLUMN PROJECTION TILING?

Row/column projection tiling means:
- The output is exactly 2× the input size in both dimensions (a 2×2 tiling)
- The input pattern is repeated/tiled to fill the output
- Background cells get replaced with a secondary "fill" color based on projection rules
- A background cell becomes the fill color if its row OR its column contains any non-background colored cell in the original input
- Non-background cells retain their original color in all tiles

Look at the training examples:
- Is the output exactly twice the size of the input in each dimension?
- Does the output look like the input tiled 2×2?
- Are there cells that changed from background to a new secondary color?
- Do the changed cells align with rows and columns that contain colored cells?

Answer ONLY with: YES or NO"""
