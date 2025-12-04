CLASSIFIER_PROMPT = """Does this puzzle exhibit SHAPE TRANSLATION WITH COLOR CHANGE?

This pattern means:
- The input contains a connected shape made of non-zero (non-background) cells
- The output contains the SAME shape but shifted/translated by a fixed offset
- The color of the shape changes from the input color to a different output color
- The shape maintains its exact form and relative cell positions

Look at the training examples:
- Is there a single connected region of non-zero cells in the input?
- Does the output have the same shape but in a different position?
- Is the shape shifted by a consistent offset (e.g., down by 1 row)?
- Does the color change from one specific color to another?
- Is the background preserved as zeros?

Answer ONLY with: YES or NO"""
