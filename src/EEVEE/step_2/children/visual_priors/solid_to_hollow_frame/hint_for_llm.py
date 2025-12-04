HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SOLID RECTANGLES → HOLLOW FRAMES              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find each solid rectangular region of non-background color
• Convert it to a hollow frame by keeping only the border
• The first row, last row, first column, and last column of each rectangle stay filled
• All interior cells (not on the perimeter) become background color

VISUAL CONCEPT:
Input:          Output:
█ █ █ █ █       █ █ █ █ █
█ █ █ █ █   →   █ ░ ░ ░ █
█ █ █ █ █       █ ░ ░ ░ █
█ █ █ █ █       █ █ █ █ █

YOUR APPROACH:
• Identify all connected rectangular regions of each non-background color
• For each rectangle, determine its bounding box
• Keep cells on the perimeter (top/bottom rows, left/right columns)
• Replace interior cells with background color
"""
