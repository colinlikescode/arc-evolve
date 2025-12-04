CLASSIFIER_PROMPT = """Does this puzzle exhibit COLORED MARKERS EXTENDED TO DIVIDER LINE?

This pattern involves:
- A horizontal divider line that spans the full width of the grid (a row filled with a single distinct color)
- The divider splits the grid into an upper region and a lower region
- Scattered marker cells of two different colors appear in both regions
- One marker color extends VERTICALLY toward the divider line (filling cells between the marker and the divider)
- The other marker color extends VERTICALLY away from the divider line (filling cells between the marker and the grid edge)

Look at the training examples:
- Is there a horizontal line of uniform color dividing the grid?
- Are there two distinct non-background colors appearing as sparse markers above and below the line?
- In the output, do markers of one color form vertical lines toward the divider?
- Do markers of the other color form vertical lines toward the nearest grid edge (top or bottom)?

Answer ONLY with: YES or NO"""
