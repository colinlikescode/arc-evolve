HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A GRID-TO-CELL SUMMARY PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into blocks by separator lines (a single color forming a grid pattern)
• Identify the separator color (forms complete horizontal and vertical lines)
• The grid of blocks forms an N×M arrangement
• The output is an N×M grid where each cell summarizes one input block

FOR EACH BLOCK:
• If the block is filled with the background color (typically 0): output the background
• If the block is filled with a non-background color: output that color as a single cell
• One column/row of blocks may be filled entirely with the SAME non-background color - this appears as a constant in that output row/column

KEY INSIGHT:
• The output captures WHICH blocks contain non-background content
• Each unique block color appears in its corresponding position in the output
• The separator lines are NOT included in the output
"""
