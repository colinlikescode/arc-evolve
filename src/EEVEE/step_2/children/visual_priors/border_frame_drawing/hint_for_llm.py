HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BORDER FRAME DRAWING PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is a uniform grid filled with the background color
• The output draws a 1-cell-thick rectangular frame around the perimeter
• The frame uses a new/different color (not the background)
• Interior cells remain as the background color

WHAT GETS THE FRAME COLOR:
• All cells in the first row (row index 0)
• All cells in the last row (row index = height - 1)
• All cells in the first column (column index 0)
• All cells in the last column (column index = width - 1)

WHAT STAYS AS BACKGROUND:
• All cells that are NOT on any edge
• These are cells where: row > 0 AND row < height-1 AND col > 0 AND col < width-1

THE OUTPUT DIMENSIONS MATCH THE INPUT DIMENSIONS EXACTLY.
"""
