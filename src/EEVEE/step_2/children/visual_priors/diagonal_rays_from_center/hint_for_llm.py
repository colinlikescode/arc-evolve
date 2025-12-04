HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL RAYS FROM CENTER POINT PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a uniform background with ONE special marker cell
• Find the position of the marker cell (the non-background value)
• In the output, draw BOTH diagonals passing through that marker position
• The diagonals extend from edge to edge of the grid

WHAT TO DO:
1. Identify the dominant/background color (fills most of the grid)
2. Find the single cell with a different value - this is the CENTER
3. Create output filled with the background color
4. Mark all cells where |row - center_row| == |col - center_col| with the marker value
5. This creates an "X" pattern centered on the marker position

THE PATTERN:
• Cells on BOTH diagonals through the center become the marker color
• All other cells remain the background color
• The marker cell itself stays as the marker color (it's on both diagonals)
"""
