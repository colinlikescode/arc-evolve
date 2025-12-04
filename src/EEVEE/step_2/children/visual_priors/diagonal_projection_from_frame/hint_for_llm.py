HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL PROJECTION FROM BOUNDED FRAME        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the frame/border structure (L-shaped or rectangular outline)
• Find the "marker" color - the distinct colored region inside or adjacent to the frame
• Locate the corner(s) of the frame that face the empty region of the grid

PROJECTION BEHAVIOR:
• From each corner of the frame facing empty space, project the marker color diagonally outward
• The diagonal extends AWAY from the bounded region into the empty space
• Each step moves one cell diagonally (both row and column change by 1)
• The direction is determined by which quadrant the empty space occupies relative to the frame

WHAT TO LOOK FOR:
• The frame's corner position determines the starting point of the diagonal
• The diagonal goes toward the nearest grid corner/edge in the empty region
• The number of cells in the diagonal relates to the available space
• The original pattern (frame + marker) remains unchanged
"""
