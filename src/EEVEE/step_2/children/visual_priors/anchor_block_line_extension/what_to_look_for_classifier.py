CLASSIFIER_PROMPT = """Does this puzzle exhibit ANCHOR BLOCK LINE EXTENSION?

This pattern involves:
- A small solid block (like 2x2) of one color acting as an "anchor"
- Scattered single cells of other colors distributed around the grid
- Lines being drawn from the anchor block's edges toward aligned markers

Look at the training examples:
- Is there a small rectangular block of uniform color (the anchor)?
- Are there isolated single cells of various colors scattered around?
- In the output, are lines drawn connecting the anchor to markers that share a row or column?
- Do the drawn lines use the color of the marker cell they extend toward?

Answer ONLY with: YES or NO"""
