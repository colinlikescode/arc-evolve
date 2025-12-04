CLASSIFIER_PROMPT = """Does this puzzle involve MARKER-DIRECTED BARRIER EXTENSION?

Look for these indicators:
- There is a solid rectangular region (barrier/wall) of a uniform color spanning part of the grid
- There are scattered individual cells of a different non-background color (markers) on one or both sides of the barrier
- The barrier can be horizontal (spanning full width) or vertical (spanning full height)
- In the output, the markers disappear and the barrier extends/grows toward where the markers were located
- The barrier extends its edge to reach each marker's position (row or column depending on barrier orientation)

Key characteristics:
- The barrier is a contiguous block of one color
- Markers are isolated cells of a different color, positioned away from the barrier
- The transformation removes markers and extends the barrier toward their locations

Answer ONLY with: YES or NO"""
