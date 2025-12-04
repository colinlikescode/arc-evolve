CLASSIFIER_PROMPT = """Does this puzzle exhibit FRAME INTERIOR FLOOD FILL WITH MARKER COLOR?

This pattern involves:
- One or more rectangular frames/boxes made of a border color (forming an incomplete or complete rectangle)
- Each frame contains a single "marker" cell of a different color somewhere inside or at the edge gap
- The interior of each frame (the empty/background cells inside) gets filled with the marker color
- The marker color also extends outward from the frame in the direction of any gap in the border

Look at the training examples:
- Are there rectangular frames made of a consistent border color?
- Does each frame have exactly one cell of a unique marker color?
- In the output, is the interior of each frame filled with that marker color?
- Does the marker color extend beyond the frame through any gaps in the border?

Answer ONLY with: YES or NO"""
