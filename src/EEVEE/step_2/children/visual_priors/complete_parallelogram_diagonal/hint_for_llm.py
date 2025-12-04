HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COMPLETE THE PARALLELOGRAM SHAPE              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a parallelogram/rhombus outline with diagonal edges
• The shape has horizontal top and bottom edges, and stair-stepped diagonal sides
• One diagonal edge is INCOMPLETE - it has gaps where cells are missing
• The output COMPLETES the shape to make both diagonal edges symmetric

HOW TO IDENTIFY THE FIX:
• Find the bounding box of the colored shape
• The left diagonal edge descends one column right per row
• The right diagonal edge should MIRROR this - descending one column right per row
• Fill in any missing cells on the right edge to complete the parallelogram
• The rightmost column of each row should align with the diagonal pattern

KEY INSIGHT:
• If left edge goes: col, col+1, col+2, col+3...
• Then right edge should go: col+W, col+W+1, col+W+2, col+W+3...
• Where W is the width of the top/bottom horizontal edge
"""
