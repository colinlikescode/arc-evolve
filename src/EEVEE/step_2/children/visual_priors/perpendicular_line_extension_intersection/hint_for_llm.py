HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LINE EXTENSION WITH INTERSECTION MARKING      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains TWO perpendicular line segments of different colors
  - One vertical segment (spans multiple rows in one column)
  - One horizontal segment (spans multiple cells in one row)

• In the output:
  - The VERTICAL line extends to fill its ENTIRE COLUMN
  - The HORIZONTAL line extends to fill its ENTIRE ROW
  - Where they INTERSECT: a third "marker" color appears

KEY OBSERVATIONS:
• Find the column containing the vertical line → extend it top to bottom
• Find the row containing the horizontal line → extend it left to right
• The intersection cell (where row meets column) gets a unique marker color

THE INTERSECTION MARKER:
• This is typically a distinct color that marks the crossing point
• It replaces what would otherwise be an ambiguous overlap
"""
