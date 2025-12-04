CLASSIFIER_PROMPT = """Does this puzzle exhibit SCALED BLOCK EXPANSION WITH MARKER?

This pattern means:
- The input is a small grid containing a special marker cell (unique color appearing once) and other non-background colored cells
- The output is N times larger in each dimension (where N = input dimension)
- Each non-background, non-marker cell in the input becomes a filled square block in the output
- The marker cell is used as a reference but does NOT appear in the output
- Block positions correspond to the original cell positions, scaled by the input dimensions

Look at the training examples:
- Is there exactly one cell with a unique "marker" color in the input?
- Is the output exactly input_size × input_size larger?
- Do the non-marker colored cells become solid filled blocks in the output?
- Is the marker color absent from the output?

Answer ONLY with: YES or NO"""
