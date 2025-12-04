CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL CASCADE/TRAIL TILING?

Diagonal cascade tiling means:
- The input is a small grid (e.g., N×M)
- The output is a larger grid, typically (2N)×(2M) or similar expansion
- The input pattern is repeatedly placed along the main diagonal
- Each copy is offset by one position down and one position to the right
- The copies overlap or tile diagonally from top-left toward bottom-right
- Background cells (zeros) fill the remaining space

Look at the training examples:
- Is the output roughly 2× the size of the input in each dimension?
- Does the input pattern appear multiple times along a diagonal?
- Is each repetition shifted by (1,1) from the previous one?
- Do the copies create a cascading/trailing effect from top-left to bottom-right?

Answer ONLY with: YES or NO"""
