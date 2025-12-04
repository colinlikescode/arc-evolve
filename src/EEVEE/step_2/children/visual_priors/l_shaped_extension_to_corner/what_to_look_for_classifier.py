CLASSIFIER_PROMPT = """Does this puzzle exhibit an L-SHAPED EXTENSION pattern?

L-shaped extension means:
- The input contains isolated non-zero cells (single colored pixels) on a background
- Each non-zero cell extends to form an "L" or reverse-"L" shape
- The horizontal part extends from the cell's position rightward to the edge of the grid
- The vertical part extends downward from the rightmost point of the horizontal extension to the bottom of the grid
- Each colored cell creates its own L-shape using its own color

Look at the training examples:
- Are there isolated single colored cells in the input?
- In the output, does each colored cell extend horizontally to the right edge?
- Does a vertical line then extend downward from the right edge?
- Do these extensions form an "L" rotated 180 degrees (or a backwards "L")?

Answer ONLY with: YES or NO"""
