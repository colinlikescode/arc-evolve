CLASSIFIER_PROMPT = """Does this puzzle involve SPARSE CELL COLLECTION INTO A COMPACT GRID?

This pattern means:
- The input is a larger grid (e.g., 10x10) with scattered non-zero cells on a zero background
- The output is a smaller grid (e.g., 3x3) that collects/compresses these scattered values
- The input grid can be conceptually divided into regions (like a 3x3 arrangement of zones)
- Each non-zero cell's position in the input determines its position in the output grid
- The transformation maps spatial regions of the input to cells of the output

Look at the training examples:
- Is the input a sparse grid with isolated non-zero cells?
- Is the output much smaller and contains the same non-zero values?
- Does the position of each value in the output correspond to which "zone" it occupied in the input?
- Are there approximately as many non-zero cells as output cells?

Answer ONLY with: YES or NO"""
