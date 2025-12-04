HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HIGHLIGHT ALL-BACKGROUND SEPARATOR LINES      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the background color (typically the most common "empty" color, often zero)
• Find all ROWS that are entirely filled with the background color
• Find all COLUMNS that are entirely filled with the background color
• Replace all cells in those separator rows/columns with a NEW marker color
• All other cells remain unchanged

WHAT TO LOOK FOR:
• Rows/columns acting as grid dividers (completely uniform background)
• These separators split the grid into rectangular regions
• The marker color is NOT present in the input - it's introduced to highlight separators

YOUR APPROACH:
1. Identify which rows are entirely background color
2. Identify which columns are entirely background color
3. Copy input to output
4. Overwrite those specific rows and columns with the marker color
"""
