CLASSIFIER_PROMPT = """Does this puzzle exhibit a 3x3 BOX EXPANSION pattern around marker cells?

This pattern means:
- The input contains scattered single cells of one specific "marker" color
- There may be other non-zero cells of different colors in the grid
- In the output, each marker cell becomes the CENTER of a 3x3 region
- The 3x3 region is filled with a new "fill" color (not present or rare in input)
- The original marker cell remains at the center of each 3x3 box
- Other non-zero cells from the input remain unchanged
- The 3x3 boxes do not overwrite other pre-existing non-zero cells

Look at the training examples:
- Is there one color that appears multiple times and gets surrounded by 3x3 boxes?
- Does a new color appear in the output forming 3x3 squares?
- Do other colored cells remain untouched?

Answer ONLY with: YES or NO"""
