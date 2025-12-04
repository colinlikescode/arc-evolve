CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL STRIPE PROPAGATION FROM A SEED POINT?

This pattern means:
- The input is mostly empty (background color) with a single non-zero "seed" cell
- The seed cell is located on the bottom row
- The output creates vertical stripes that extend upward from the seed position to the top of the grid
- The stripes continue horizontally to the right edge of the grid in a repeating pattern
- The pattern uses the seed color for vertical lines and a secondary marker color at specific corners/intersections

Look at the training examples:
- Is there exactly one non-zero cell in the input, located on the bottom row?
- Does the output show vertical columns of the seed color extending from bottom to top?
- Do these vertical stripes repeat horizontally from the seed column to the right edge?
- Is there a secondary color marking certain corner positions in the pattern?

Answer ONLY with: YES or NO"""
