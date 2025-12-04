CLASSIFIER_PROMPT = """Does this puzzle exhibit SPLIT-GRID UNION/OR COMBINATION?

This pattern involves:
- The input grid is divided into two equal halves (left and right, or top and bottom)
- Each half contains a distinct marker color (different non-background colors in each half)
- The output grid has the same dimensions as ONE half
- The output marks positions where EITHER half has a non-background cell
- All marked positions in the output use a single unified color

Look at the training examples:
- Is the input grid twice as wide (or tall) as the output?
- Are there two distinct non-background colors, each confined to one half of the input?
- Does the output appear to be a logical OR/union of the patterns from both halves?
- Are all non-background cells in the output the same color (different from input colors)?

Answer ONLY with: YES or NO"""
