CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL EMANATING RAYS FROM A SINGLE POINT?

This pattern means:
- The input contains a single non-background cell (a "seed" or "center" point)
- The output keeps this seed cell in place
- From the seed, two diagonal rays extend outward in opposite directions (e.g., upper-right and lower-left)
- Each ray consists of a repeating L-shaped or corner pattern using a secondary color
- The rays grow outward from the seed, with each segment stepping diagonally away
- The pattern continues until it reaches or approaches the grid boundary

Look at the training examples:
- Is there exactly one non-background cell in the input?
- In the output, do diagonal patterns emanate from that cell's position?
- Are there L-shaped or corner segments that repeat along two opposite diagonal directions?
- Does a secondary color appear in the output forming these diagonal ray patterns?

Answer ONLY with: YES or NO"""
