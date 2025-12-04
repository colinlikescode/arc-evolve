CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER EXPANSION FROM MARKER?

This pattern means:
- The input contains a single non-zero "marker" cell on a background of zeros
- The output removes the marker and places a fixed set of four distinct colors at diagonal positions around where the marker was
- The four colors form a 2x2 pattern centered on the marker's original position
- Colors that would fall outside the grid boundaries are simply not placed

Look at the training examples:
- Is there exactly one non-zero cell in each input?
- Does the output have the marker removed (replaced with zero)?
- Do new colors appear at the four diagonal neighbors of the marker position?
- Are the same four colors used consistently across all examples in the same relative positions?

Answer ONLY with: YES or NO"""
