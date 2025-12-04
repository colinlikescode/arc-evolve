CLASSIFIER_PROMPT = """Does this puzzle exhibit a GRID-TO-CELL SUMMARY pattern?

This pattern involves:
- The input is divided into a grid of rectangular cells/blocks by separator lines (a single repeating color forming horizontal and vertical dividers)
- Each cell block contains a uniform fill of some color (could be background or a distinct color)
- The output is a small grid where each cell corresponds to one block from the input
- Each output cell contains a SINGLE representative value extracted from the corresponding input block

Look at the training examples:
- Is the input divided into a regular grid by lines of a single separator color?
- Does each resulting block contain a uniform solid color?
- Is the output much smaller than the input (one cell per block)?
- Does each output cell represent the content/color of its corresponding input block?
- Are blocks filled with the background color represented differently than blocks with other colors?

Answer ONLY with: YES or NO"""
