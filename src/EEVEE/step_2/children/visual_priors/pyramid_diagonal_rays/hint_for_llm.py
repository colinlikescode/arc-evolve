HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PYRAMID WITH UPWARD DIAGONAL RAYS             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a pyramid/triangular base at the bottom
• The base has TWO colors: an "outer" color (on the wings) and an "inner" color (at center)
• The original base structure remains UNCHANGED in the output

DIAGONAL RAY EMISSION:
• Find where the "outer" color segments meet the edges of the grid (left and right sides)
• From these corner points, draw diagonal lines going UPWARD and OUTWARD
• Left diagonal goes up-left, right diagonal goes up-right
• The diagonals use the "inner" color (center color from bottom row)
• Continue until reaching the grid boundary

KEY INSIGHT:
• The number of diagonal steps equals the distance from the pyramid edge to the grid edge
• The rays form a V-shape opening upward from the pyramid's outer edges
"""
