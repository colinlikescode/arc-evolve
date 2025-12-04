CLASSIFIER_PROMPT = """Does this puzzle exhibit GAP-FILLING BETWEEN ADJACENT RECTANGLES?

This pattern involves:
- Multiple rectangular regions of a non-background color scattered across the grid
- Some rectangles are positioned such that they share rows or columns (horizontally or vertically aligned)
- When two rectangles are aligned (same rows or same columns), the gap between them gets filled with a marker color

Look at the training examples:
- Are there multiple rectangular blocks of the same non-background color?
- Do some rectangles share the same row span (horizontally adjacent) or column span (vertically adjacent)?
- Is the empty space BETWEEN aligned rectangles filled with a new color in the output?
- Does the fill only appear where rectangles are "facing" each other across a gap?

Answer ONLY with: YES or NO"""
