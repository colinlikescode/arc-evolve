CLASSIFIER_PROMPT = """Does this puzzle exhibit TWO-POINT EXPANSION WITH MEETING CROSS PATTERN?

This pattern has the following characteristics:
- The input contains exactly TWO non-zero colored cells on a background of zeros
- These two cells are separated by some distance (horizontally, vertically, or diagonally)
- The output shows each colored cell "growing" toward the other
- Each color forms a cross or L-shape that extends from its original position toward the midpoint
- The two colored structures meet in the middle, creating a symmetric bow-tie or hourglass-like shape
- The arms of each cross extend perpendicular to the line connecting the two original points

Look at the training examples:
- Are there exactly two differently-colored non-zero cells in the input?
- Does the output show expanded cross/L-shapes for each color?
- Do the shapes meet at the midpoint between the two original cells?
- Is there point symmetry around the center of the two original points?

Answer ONLY with: YES or NO"""
