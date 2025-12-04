HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL INTERIOR OF CORNER-MARKED RECTANGLES    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find groups of 4 marker cells that form rectangle corners
• Each rectangle is defined by markers at positions forming a rectangular boundary
• The INTERIOR region (inside the corners, not including edges with markers) gets filled
• Fill color is a DIFFERENT color from the marker color
• Corner markers REMAIN in place - only the interior changes

HOW TO IDENTIFY RECTANGLES:
• Look for 4 markers where two share the same row AND two share the same column
• The markers define: (top-row, left-col), (top-row, right-col), (bottom-row, left-col), (bottom-row, right-col)

WHAT TO FILL:
• The rectangular region STRICTLY INSIDE the corner positions
• From (top-row + 1) to (bottom-row - 1) in rows
• From (left-col + 1) to (right-col - 1) in columns
• Fill with a secondary/accent color (not the marker color, not background)
"""
