HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-BASED GRID LINE PROJECTION             ║
╚══════════════════════════════════════════════════════════════╝

THE STRUCTURE:
• Input has nested rectangular regions: background → frame color → inner fill color
• "Marker" cells are isolated cells of the inner color appearing in the frame layer

THE TRANSFORMATION RULE:
• Find marker cells (inner fill color appearing where frame color should be)
• Each marker defines a row OR column position for a dividing line
• Draw lines through the entire structure at each marker position:
  - INSIDE the frame: use the frame color (subdividing the inner region)
  - OUTSIDE the frame: use the inner fill color (extending into background)
• Lines extend from edge of grid to edge of grid through marker positions
• The inner filled region becomes a grid pattern divided by frame-colored lines

KEY INSIGHT:
• Markers on TOP/BOTTOM edges → vertical lines at that column
• Markers on LEFT/RIGHT edges → horizontal lines at that row
• Lines replace both the inner fill (with frame color) AND background (with inner color)
"""
