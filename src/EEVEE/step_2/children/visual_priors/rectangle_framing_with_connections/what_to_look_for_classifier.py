CLASSIFIER_PROMPT = """Does this puzzle exhibit RECTANGLE BOUNDING BOX WITH CONNECTION LINES?

This pattern involves:
- Multiple rectangular regions filled with a single non-background color scattered across the grid
- In the output, each rectangle gets surrounded by a "frame" or "border" of a secondary color
- Rectangles are connected to each other via straight lines (horizontal/vertical) using a third color
- The connection lines extend from rectangles toward each other, typically aligned with the rectangle centers or edges
- The original rectangles remain intact while decorative framing and connecting elements are added

Look at the training examples:
- Are there multiple isolated rectangular blocks of the same color in the input?
- In the output, do these rectangles gain borders/frames around them?
- Are there straight lines connecting the rectangular regions?
- Do the connections appear to link rectangles in a network-like pattern?

Answer ONLY with: YES or NO"""
