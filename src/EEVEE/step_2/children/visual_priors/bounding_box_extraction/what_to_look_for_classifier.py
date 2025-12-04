CLASSIFIER_PROMPT = """Does this puzzle exhibit BOUNDING BOX EXTRACTION?

Bounding box extraction means:
- The input is a larger grid with mostly background (zero) cells
- There is a connected or clustered pattern of non-zero cells somewhere in the grid
- The output extracts just the minimal bounding rectangle that contains ALL non-zero cells
- The output preserves the exact pattern of non-zero and zero cells within that bounding box

Look at the training examples:
- Is the input a sparse grid with a small pattern of colored cells surrounded by background?
- Is the output much smaller than the input?
- Does the output appear to be the "cropped" version containing only the region with non-zero cells?
- Are the relative positions of non-zero cells preserved exactly in the output?

Answer ONLY with: YES or NO"""
