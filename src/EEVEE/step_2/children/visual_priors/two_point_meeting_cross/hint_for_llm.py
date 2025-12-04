HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TWO-POINT MEETING CROSS EXPANSION            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero colored cells in the input
• Calculate the MIDPOINT between them
• Each color expands from its original position TOWARD the midpoint
• Each color forms a CROSS shape:
  - A line from the original cell toward (but not past) the midpoint
  - A perpendicular bar at the point closest to the midpoint
  - The bar width equals the perpendicular distance to the midpoint

STRUCTURE OF EACH COLOR'S SHAPE:
• Main arm: extends from original position toward center
• Cross bar: perpendicular line at the end closest to midpoint
• The two colors' shapes are POINT-SYMMETRIC around the midpoint
• They share a boundary region but don't overlap

KEY INSIGHT:
• The distance from each original cell to the midpoint determines arm length
• The perpendicular offset determines the cross bar extent
• Both shapes "reach toward" each other and meet in the middle
"""
