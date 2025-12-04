CLASSIFIER_PROMPT = """Does this puzzle exhibit CROSS-DIVIDED QUADRANT EXTRACTION?

Cross-divided quadrant extraction means:
- The input grid is divided into quadrants by a full horizontal line and a full vertical line of a single "divider" color
- These divider lines span the entire width and height of the grid, forming a cross/plus shape
- The divider lines split the grid into 4 rectangular regions (quadrants)
- One of the quadrants contains a unique "marker" cell - a cell with a color different from both the dominant background color AND the divider color
- The output is that specific quadrant (without the divider lines)

Look at the training examples:
- Is there a complete row of one color AND a complete column of that same color that intersect?
- Do these lines divide the grid into 4 regions?
- Is there exactly one cell in one quadrant that has a unique/different color?
- Is the output one of those quadrant regions?

Answer ONLY with: YES or NO"""
