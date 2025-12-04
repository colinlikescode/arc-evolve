CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE STAMPING based on MARKER ALIGNMENT?

Template stamping with marker alignment means:
- The input contains a rectangular region filled with one color (the "template") that has scattered marker cells of another color embedded within it
- The input also has isolated marker cells scattered throughout the grid (same color as markers in template)
- The transformation finds locations where scattered markers match the relative positions of markers inside the template
- At those matching locations, a copy of the template rectangle is drawn, aligning the template's internal markers with the scattered markers

Look at the training examples:
- Is there a filled rectangular region with a distinct marker color inside it?
- Are there isolated marker cells scattered elsewhere in the grid?
- In the output, do new copies of the filled rectangle appear at locations where scattered markers existed?
- Do the marker positions inside new rectangles correspond to where scattered markers were?

Answer ONLY with: YES or NO"""
