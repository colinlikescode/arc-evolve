CLASSIFIER_PROMPT = """Does this puzzle exhibit a BOUNDED REGION FILL WITH LEAK/ESCAPE pattern?

Look for these indicators:
- There is a closed or nearly-closed rectangular frame/border made of a non-zero color
- The frame has one or more GAPS (missing cells in what would otherwise be a complete border)
- The interior region enclosed by the frame contains background (zero) cells
- In the output, the interior gets filled with a NEW color
- The fill color also "leaks" or "escapes" through the gap(s), extending outward in a line to the grid boundary

Key structural elements:
- A rectangular boundary shape with intentional breaks/openings
- The transformation fills the interior AND extends through the openings
- The leak creates a straight line from the gap toward the edge of the grid

Answer ONLY with: YES or NO"""
