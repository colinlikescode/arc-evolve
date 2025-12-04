CLASSIFIER_PROMPT = """Does this puzzle exhibit GRAVITY/FALLING OBJECTS TO A SURFACE?

Look for these indicators:
- There is a horizontal "ground" or "floor" line (a row filled with one consistent color) at or near the bottom
- Above the ground, there are vertical "columns" or "stacks" of cells
- Some cells appear to be "floating" above the ground with markers below them
- In the output, these floating objects have moved downward to rest on the ground
- The objects maintain their horizontal (column) position but change vertical position
- Cells that were occupied by falling objects become background in the output

The transformation simulates gravity: objects fall straight down until they hit the ground/surface.

Answer ONLY with: YES or NO"""
