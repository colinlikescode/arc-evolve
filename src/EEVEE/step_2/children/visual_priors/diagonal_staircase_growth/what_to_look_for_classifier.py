CLASSIFIER_PROMPT = """Does this puzzle exhibit a DIAGONAL STAIRCASE GROWTH pattern?

Diagonal staircase growth means:
- The input is a single row (1×N grid)
- The input contains a contiguous block of non-zero colored cells starting from the left, followed by zeros
- The output expands vertically into multiple rows
- Each subsequent row adds one more colored cell to the right, creating a diagonal "staircase" edge
- The number of output rows equals the number of zero cells in the input plus one (or equivalently, the output fills until the colored region reaches the right edge or a specific boundary)

Look at the training examples:
- Is the input a single horizontal row?
- Does the input have colored cells on the left and zeros on the right?
- Does the output grow downward with each row extending the colored region by one cell?
- Does the boundary between colored and zero cells form a diagonal line going down-right?

Answer ONLY with: YES or NO"""
