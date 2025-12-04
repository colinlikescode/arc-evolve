CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID-DIVIDED PATTERN COMPLETION WITH REFERENCE SHAPE?

This pattern type means:
- The grid is divided into rectangular cells/regions by horizontal and vertical lines of a single "divider" color
- One cell contains a complete "reference shape" made of a secondary color
- Other cells contain partial/incomplete versions of this shape (fragments)
- Empty cells (no shape fragments) exist in the grid

Look at the training examples:
- Is there a grid structure created by lines of one color dividing the space into equal rectangular regions?
- Is there one region that contains a complete, recognizable shape?
- Do other regions contain partial fragments of shapes?
- Are there regions that are completely empty (just background)?

The transformation involves using the reference shape to determine what should appear in cells based on their fragment content.

Answer ONLY with: YES or NO"""
