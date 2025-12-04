HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID-DIVIDED UNIQUE COLOR BLOCK FILL         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into blocks by separator lines (rows/columns of a single repeated color)
• For each block, identify which non-zero, non-separator colors appear ONLY in that block and no other block
• Fill the entire block uniformly with that unique color
• If a block has no unique color (all its colors appear elsewhere), fill it with zeros
• Separator lines remain unchanged

HOW TO FIND THE UNIQUE COLOR:
• For each block, collect all distinct non-zero, non-separator colors
• Compare with colors in ALL other blocks
• The unique color is the one that exists ONLY in this block
• Each block gets filled with its unique color (or zeros if none)

KEY INSIGHT:
The puzzle tests whether you can identify which color is "exclusive" to each region by comparing across all regions.
"""
