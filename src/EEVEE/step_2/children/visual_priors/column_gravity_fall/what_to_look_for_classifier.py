CLASSIFIER_PROMPT = """Does this puzzle exhibit COLUMN-WISE GRAVITY (falling cells)?

Column-wise gravity means:
- Non-zero cells in each column "fall down" toward the bottom of the grid
- The relative vertical order of non-zero cells within each column is preserved
- Zero/background cells effectively "bubble up" to fill the top of each column
- Each column is processed independently

Look at the training examples:
- Do non-zero cells appear to have moved downward in the output?
- Are the non-zero cells in each column now stacked at the bottom?
- Is the horizontal position (column) of each colored cell preserved?
- Do the top rows become mostly or entirely filled with zeros?

Answer ONLY with: YES or NO"""
