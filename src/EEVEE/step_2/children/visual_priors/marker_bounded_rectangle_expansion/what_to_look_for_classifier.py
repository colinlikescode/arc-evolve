CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-BOUNDED RECTANGLE EXPANSION?

Marker-bounded rectangle expansion means:
- There is a small rectangular shape made of a non-background, non-marker color in the input
- There are exactly 4 marker cells (a distinct secondary color) scattered around the grid
- These 4 markers define the corners of a larger bounding rectangle
- The output draws a larger rectangle connecting the 4 markers using the same color as the original shape
- The original small shape remains in place inside the larger rectangle
- The markers themselves remain unchanged in the output

Look at the training examples:
- Is there a small rectangular frame/outline shape in the input?
- Are there exactly 4 isolated single-cell markers of a different color?
- Do these markers appear to define the corners of a larger rectangular region?
- Does the output show a larger rectangle drawn between the markers, with the original shape preserved inside?

Answer ONLY with: YES or NO"""
