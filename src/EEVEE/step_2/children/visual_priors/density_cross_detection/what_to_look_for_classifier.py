CLASSIFIER_PROMPT = """Does this puzzle involve DENSITY-BASED CROSS PATTERN DETECTION?

This pattern type means:
- The input is a grid with scattered non-zero colored cells on a black background
- The output is a smaller grid (typically 3x3) showing a cross or plus-shaped pattern
- The output uses a single indicator color (replacing the input's colored cells)
- The orientation/shape of the cross in the output reflects the spatial distribution or density of colored cells in different regions of the input
- Different inputs with the same color but different distributions produce different cross orientations

Look at the training examples:
- Are the inputs larger grids with scattered colored cells?
- Are the outputs smaller grids showing cross/plus/T-shaped patterns?
- Does the output use a uniform indicator color (not the original input color)?
- Do different spatial distributions of input cells produce different cross orientations?

Answer ONLY with: YES or NO"""
