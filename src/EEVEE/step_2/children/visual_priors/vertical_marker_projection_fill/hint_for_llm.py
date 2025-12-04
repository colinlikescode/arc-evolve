HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL MARKER PROJECTION INTO SHAPE HOLES   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the main shape (made of one non-background color)
• Identify marker cells (a different non-background color, typically below/outside the shape)
• For each column containing markers: project upward
• Where the projection intersects a HOLE (background cell) WITHIN the shape's bounding region, fill that hole with the marker color
• Clear the original marker cells that were outside the shape region

KEY CONCEPTS:
• Markers act like "rays" shooting vertically toward the shape
• Only holes INSIDE the shape get filled - the marker "stops" there
• The number of markers in a column determines how many holes get filled in that column (from bottom-up within the shape)
• Original markers below/outside the shape are erased

THINK OF IT AS: Markers rise up and "plug" the holes in the shape above them.
"""
