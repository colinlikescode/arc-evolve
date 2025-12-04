CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL LINE EXPANSION FROM A SINGLE POINT?

This pattern means:
- The input contains exactly ONE non-zero cell (a single colored pixel) on a background of zeros
- The output draws diagonal lines emanating from that single point
- Lines extend in BOTH diagonal directions (↘ and ↗) from the point
- The lines continue until they reach the grid boundaries
- The original point remains in place
- An "X" pattern forms centered on the original point, with arms extending to grid edges

Look at the training examples:
- Is there exactly one non-zero cell in the input?
- Does the output show diagonal lines (45-degree angles) passing through that cell's position?
- Do the lines extend from the point toward all four diagonal corners of the grid?
- Does the pattern form an X shape centered on the original point?

Answer ONLY with: YES or NO"""
