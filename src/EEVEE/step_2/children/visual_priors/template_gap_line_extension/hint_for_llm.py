HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTEND LINES FROM TEMPLATE SHAPE GAPS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify TWO distinct non-background colors:
  - One color forms a connected TEMPLATE SHAPE (funnel/bracket-like)
  - Another color appears as scattered MARKER CELLS

• Find the template shape's BOTTOM ROW (its widest/lowest extent)

• Within that bottom row of the shape, identify the GAP POSITIONS
  (cells that are background color but lie between the shape's edges)

• From each gap position, draw a VERTICAL LINE downward using the
  MARKER COLOR, extending to the bottom edge of the grid

• Keep all original cells unchanged - only ADD the new vertical lines

KEY INSIGHT: The shape acts like a "funnel" - the gaps in its opening
determine where vertical lines will be drawn downward.
"""
