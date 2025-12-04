CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID CELL MARKER-TO-FILL-COLOR MAPPING?

This pattern involves:
- A grid divided into rectangular sections by separator lines (a consistent divider color)
- Each section contains a single marker cell (a non-background, non-separator colored cell)
- The marker's color value determines what fill color the entire section becomes
- There is a consistent mapping: marker_value → output_fill_color (e.g., value N maps to fill color N+5)

Look at the training examples:
- Is the grid divided into rectangular regions by lines of a single separator color?
- Does each region have exactly one colored marker cell (not the separator or background)?
- In the output, is each region filled uniformly with a single color?
- Does the fill color appear to be computed from the marker's color value using a fixed offset or formula?
- Are the separator lines preserved in the output?

Answer ONLY with: YES or NO"""
