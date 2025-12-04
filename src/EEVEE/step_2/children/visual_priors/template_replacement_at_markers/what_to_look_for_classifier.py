CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE REPLACEMENT AT MARKER LOCATIONS?

Template replacement means:
- There is a small "template" pattern made of multiple distinct colors (NOT the marker color)
- There are several "marker" regions made of a single uniform color (the marker color)
- The marker regions have the SAME SHAPE as the template pattern
- In the output, each marker region is REPLACED by the template pattern (preserving position/shape)
- The original template location becomes empty/background in the output

Look at the training examples:
- Is there one multi-colored pattern (the template) with 2+ distinct non-background colors?
- Are there multiple single-colored regions (markers) that match the template's shape?
- In the output, do the marker regions get replaced by copies of the template?
- Does the original template location become background/zeros?

Answer ONLY with: YES or NO"""
