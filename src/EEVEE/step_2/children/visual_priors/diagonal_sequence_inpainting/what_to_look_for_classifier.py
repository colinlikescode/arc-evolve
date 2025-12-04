CLASSIFIER_PROMPT = """Does this puzzle exhibit a DIAGONAL SEQUENCE PATTERN WITH MASKED REGIONS?

This pattern means:
- The grid contains a repeating diagonal sequence pattern where each cell's value depends on its position
- The value at position (row, col) follows a formula like: (row + col) mod N + offset, creating diagonal stripes
- Some rectangular regions are masked with zeros (the background/mask color)
- The output restores the complete diagonal sequence pattern by filling in the masked regions

Look at the training examples:
- Does the non-zero portion of the grid show a diagonal pattern where values increase along diagonals?
- Are there rectangular regions filled with zeros that interrupt this pattern?
- Does the output show a complete, uninterrupted diagonal sequence pattern?
- Is the sequence cyclic (wrapping around after reaching a maximum value)?

Answer ONLY with: YES or NO"""
