CLASSIFIER_PROMPT = """Does this puzzle exhibit a DIRECTIONAL RAY EXTENSION pattern?

A directional ray extension pattern means:
- There is a shape/cluster of cells with a dominant color
- Within or at the edge of this shape, there is exactly ONE cell of a different "marker" color
- The marker cell is positioned at a specific location relative to the shape (e.g., at the tip, edge, or apex)
- The shape has a clear directional orientation (like an arrow or triangle pointing in a direction)
- The transformation extends a LINE/RAY from the marker cell in the direction the shape "points"
- This ray continues to the edge of the grid, filling cells with the marker color

Look at the training examples:
- Is there a triangular or arrow-like shape made of one color?
- Is there a single cell of a different color embedded in or adjacent to this shape?
- Does the shape suggest a direction (like an arrowhead)?
- In the output, is there a line extending from the marker cell toward the grid boundary in the direction the shape points?

Answer ONLY with: YES or NO"""
