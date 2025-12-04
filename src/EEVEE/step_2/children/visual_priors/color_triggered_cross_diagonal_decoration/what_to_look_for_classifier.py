CLASSIFIER_PROMPT = """Does this puzzle exhibit COLOR-SPECIFIC CROSS/DIAGONAL MARKER PATTERNS?

This pattern type means:
- The input contains scattered single-cell markers of different colors on a background
- Each distinct marker color triggers a DIFFERENT decorative pattern to be added around it
- One marker color causes a CROSS pattern (4 cells in cardinal directions: up, down, left, right)
- Another marker color causes a DIAGONAL pattern (4 cells in diagonal directions: corners)
- The original markers remain in place
- Other colored cells that don't match these two specific marker types remain unchanged

Look at the training examples:
- Are there isolated single-cell colored markers scattered on a black/zero background?
- Do some markers get surrounded by a cross pattern (+ shape) of a new color?
- Do other markers get surrounded by a diagonal pattern (X shape) of a different new color?
- Do any other colored cells remain unchanged (no pattern added)?
- Are exactly two marker types transformed, each with their own output pattern and output color?

Answer ONLY with: YES or NO"""
