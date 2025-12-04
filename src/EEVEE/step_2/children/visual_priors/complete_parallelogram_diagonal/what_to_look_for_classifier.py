CLASSIFIER_PROMPT = """Does this puzzle involve COMPLETING A PARALLELOGRAM/RHOMBUS SHAPE?

Look for these indicators:
- There is a diagonal shape (parallelogram, rhombus, or slanted rectangle) formed by non-zero cells
- The shape has two horizontal edges (top and bottom) and two diagonal edges
- The diagonal edges are "stair-stepped" - each row shifts by one column
- The shape appears incomplete or asymmetric - one diagonal edge may have gaps/missing cells
- The transformation fills in or adjusts cells to make the shape symmetric/complete

Specifically check:
- Is there a shape where the top-left to bottom-left edge and top-right to bottom-right edge should mirror each other diagonally?
- Are there missing cells on one of the diagonal edges that need to be filled?
- Does the shape need to be "squared off" to form a proper parallelogram?

Answer ONLY with: YES or NO"""
