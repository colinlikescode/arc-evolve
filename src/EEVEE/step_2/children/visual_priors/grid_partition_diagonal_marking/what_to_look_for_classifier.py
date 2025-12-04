CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID PARTITIONING WITH DIAGONAL CELL MARKING?

This pattern means:
- The input grid has a single dominant "divider" color that forms horizontal and vertical lines
- These divider lines partition the grid into rectangular cell regions (like a tic-tac-toe board but potentially with more divisions)
- The background cells (non-divider regions) are filled with a uniform background color
- The transformation marks certain cell regions along the diagonal with distinct new colors

Look at the training examples:
- Is there a consistent color forming horizontal and vertical lines that divide the grid?
- Do these lines create a regular grid of rectangular regions?
- In the output, are exactly three cell regions filled with new colors?
- Are the filled regions positioned along the diagonal (top-left corner, middle, bottom-right corner)?

Answer ONLY with: YES or NO"""
