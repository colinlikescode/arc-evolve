HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS PUZZLE EXTRACTS THE CENTER COLUMN        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The output has the SAME dimensions as the input
• ONLY the center column is preserved from the input
• ALL other columns are replaced with zeros (background)

HOW TO FIND THE CENTER COLUMN:
• For a grid with width W, the center column index is W // 2
• (Integer division gives the middle index)

YOUR APPROACH:
1. Identify the center column index (width divided by 2, integer)
2. Create an output grid of the same size, filled with zeros
3. Copy ONLY the center column values from input to output
4. All non-center-column positions remain zero

The transformation isolates the vertical spine/axis of the grid.
"""
