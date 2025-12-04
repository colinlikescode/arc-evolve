HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID PARTITION - EXTRACT LARGEST CELL         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid has DIVIDER LINES (rows/columns of a single color)
• These dividers partition the grid into rectangular CELLS
• Find the cell with the LARGEST AREA (most rows × most columns)
• The output is that cell's dimensions, filled with the FILL COLOR

HOW TO IDENTIFY:
• Divider color: forms complete horizontal/vertical lines
• Fill color: the other color that fills the spaces between dividers
• Cells: rectangular regions bounded by dividers or grid edges

YOUR APPROACH:
1. Identify which color forms the divider lines (full rows/columns)
2. Find all row indices and column indices where dividers occur
3. Calculate the dimensions of each cell between dividers
4. Find the cell with maximum area (height × width)
5. Output a rectangle of that size filled with the fill color
"""
