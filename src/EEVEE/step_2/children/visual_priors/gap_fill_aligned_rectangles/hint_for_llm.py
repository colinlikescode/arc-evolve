HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GAP-FILLING BETWEEN ALIGNED RECTANGLES        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains multiple rectangular regions of a primary non-background color
• Find pairs of rectangles that are ALIGNED:
  - Horizontally aligned: share the same row range (overlapping rows)
  - Vertically aligned: share the same column range (overlapping columns)
• For each aligned pair, fill the GAP between them with a marker color
• The fill occupies only the OVERLAPPING row/column span between the two rectangles

HOW TO IDENTIFY GAPS TO FILL:
• Two rectangles facing each other horizontally → fill the horizontal gap in their shared rows
• Two rectangles facing each other vertically → fill the vertical gap in their shared columns
• Only fill background cells; do not overwrite existing colored cells

THE MARKER COLOR:
• A new color (not the background, not the rectangle color) appears only in the gaps
• This creates "bridges" or "connections" between aligned rectangles
"""
