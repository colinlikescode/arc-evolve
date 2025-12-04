HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BORDER INTERSECTION GRID FILLING              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has TWO border colors forming corner/L-shaped regions on adjacent edges
• There is an interior region filled with background color (typically black/zero)
• Find the "transition rows" and "transition columns" - these are the positions where:
  - The border on one edge reaches its maximum penetration into the interior
  - The border on the adjacent edge reaches its maximum penetration

HOW TO IDENTIFY THE LINES:
• For each edge's border: find where it transitions from "all border" to "mixed/interior"
• Draw horizontal lines at rows where one border's depth changes significantly
• Draw vertical lines at columns where the other border's depth changes significantly
• Fill these line positions with a new fill color (replacing background cells only)

THE RESULT:
• A cross or grid pattern of the fill color appears in the interior
• The fill color only replaces background cells, not border cells
• The lines mark the "meeting boundaries" between the two border regions
"""
