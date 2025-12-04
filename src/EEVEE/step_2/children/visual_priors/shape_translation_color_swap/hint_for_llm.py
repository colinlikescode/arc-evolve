HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SHAPE TRANSLATION WITH COLOR REPLACEMENT      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all non-zero (non-background) cells in the input - they form a shape
• Translate/shift the entire shape by a fixed offset (typically 1 cell down)
• Replace the original color with a different designated output color
• The background remains unchanged (zeros)

KEY OBSERVATIONS:
• The shape's structure is PRESERVED exactly
• Only the POSITION changes (shifted down by 1 row)
• The COLOR changes from input color → output color
• Grid dimensions remain the same

YOUR APPROACH:
1. Identify all cells with the non-zero color in the input
2. For each such cell at (row, col), place the output color at (row + offset, col)
3. All other cells remain as background (zero)

The offset direction appears to be consistently DOWN by 1 row.
"""
