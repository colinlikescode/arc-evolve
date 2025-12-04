CLASSIFIER_PROMPT = """Does this puzzle exhibit UPWARD DIAGONAL RAYS FROM A PYRAMID BASE?

This pattern means:
- There is a triangular/pyramid-like structure at the bottom of the grid
- The pyramid has two colors: an "outer" color forming the sides/wings and an "inner" color at the center
- The bottom row is wider than the row above it, creating a stepped pyramid shape
- In the output, diagonal lines extend UPWARD and OUTWARD from the corners of the pyramid
- These diagonal rays use the "inner" color (the center color from the bottom row)
- The original pyramid structure remains unchanged

Look at the training examples:
- Is there a stepped pyramid pattern at the bottom with two distinct colors?
- Do diagonal lines appear in the output extending upward from the pyramid edges?
- Are the diagonals made of the same color as the center of the bottom row?

Answer ONLY with: YES or NO"""
