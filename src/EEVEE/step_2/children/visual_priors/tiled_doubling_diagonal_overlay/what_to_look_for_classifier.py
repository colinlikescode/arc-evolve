CLASSIFIER_PROMPT = """Does this puzzle exhibit TILED DOUBLING WITH DIAGONAL MARKER OVERLAY?

This pattern means:
- The output is exactly 2x the size of the input in both dimensions (width doubles, height doubles)
- The input pattern is tiled/repeated 2x2 to fill the output
- A secondary "marker" color appears in the output at positions that form diagonal lines connecting the non-zero/non-background colored cells from the input
- The original non-background colored cells are preserved at their tiled positions
- The marker color creates diagonal paths or checkerboard-like patterns between the special colored cells

Look at the training examples:
- Is the output exactly twice as wide and twice as tall as the input?
- Are the original colored cells (non-zero, non-background) preserved and repeated in a 2x2 tiling?
- Does a new color appear that wasn't in the input, forming diagonal line patterns?
- Do these diagonal patterns seem to connect or relate to the positions of the original colored cells?

Answer ONLY with: YES or NO"""
