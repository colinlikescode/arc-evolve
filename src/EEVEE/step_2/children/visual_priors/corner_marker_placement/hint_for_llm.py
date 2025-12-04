HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CORNER MARKER PLACEMENT PATTERN               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all rectangular blocks of a non-background color in the input
• For each block, add four colored corner markers at diagonal positions
• The markers go ONE cell diagonally outward from each corner of the block

MARKER PLACEMENT (relative to block bounds):
• TOP-LEFT marker: one row above, one column left of block's top-left corner
• TOP-RIGHT marker: one row above, one column right of block's top-right corner  
• BOTTOM-LEFT marker: one row below, one column left of block's bottom-left corner
• BOTTOM-RIGHT marker: one row below, one column right of block's bottom-right corner

IMPORTANT:
• Each corner position uses a DIFFERENT color
• The same four colors are used consistently across ALL blocks
• The original blocks remain unchanged in the output
• Markers use the same relative color assignment for all blocks (e.g., top-left is always the same color)
"""
