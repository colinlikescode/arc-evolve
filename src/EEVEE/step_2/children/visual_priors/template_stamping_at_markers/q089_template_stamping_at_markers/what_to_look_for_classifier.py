CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE STAMPING AT MARKER LOCATIONS?

Template stamping means:
- There is one complete "template" shape in the input (a small connected pattern with multiple colors)
- There are isolated single-cell "markers" scattered elsewhere in the grid (using a specific marker color)
- The marker color appears BOTH as part of the template AND as isolated single cells
- In the output, the complete template pattern is copied/stamped at each isolated marker location
- The template is positioned so that the marker color cell in the template aligns with the marker position

Look at the training examples:
- Is there one multi-cell connected shape that serves as a template?
- Are there isolated single cells of a particular color elsewhere in the grid?
- Does that marker color also appear within the template shape?
- In the output, does the template appear at each marker location?
- Does the original template remain unchanged in the output?

Answer ONLY with: YES or NO"""
