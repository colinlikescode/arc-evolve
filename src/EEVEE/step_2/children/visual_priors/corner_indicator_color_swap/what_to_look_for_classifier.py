CLASSIFIER_PROMPT = """Does this puzzle exhibit COLOR REPLACEMENT WITH CORNER INDICATOR?

This pattern means:
- There is a shape/pattern made of one non-zero color in the main area of the grid
- There is a single isolated cell of a DIFFERENT non-zero color in a corner (typically bottom-left)
- The isolated corner cell acts as an "indicator" or "replacement color"
- The output replaces ALL cells of the main pattern color with the indicator color
- The corner indicator cell itself becomes background (zero) in the output

Look at the training examples:
- Is there a connected shape made of one color in the interior of the grid?
- Is there a single isolated pixel of a different color in one of the corners?
- Does the output show the same shape but with the color changed to match the corner indicator?
- Does the corner cell disappear (become background) in the output?

Answer ONLY with: YES or NO"""
