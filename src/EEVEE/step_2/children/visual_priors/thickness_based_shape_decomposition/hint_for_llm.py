HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THICKNESS-BASED SHAPE DECOMPOSITION          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The shape is split into "thick" and "thin" regions based on 2x2 block membership
• A cell is "thick" if it is part of ANY 2x2 block of non-zero cells in the input
• A cell is "thin" if it is non-zero but NOT part of any 2x2 block

COLOR ASSIGNMENT:
• "Thick" cells (part of 2x2 blocks) → one output color
• "Thin" cells (not part of any 2x2 block) → different output color
• Background cells remain background

HOW TO CHECK 2x2 MEMBERSHIP:
For each non-zero cell at (r, c), check if it participates in ANY of the four possible 2x2 blocks:
- Top-left corner: (r, c), (r, c+1), (r+1, c), (r+1, c+1)
- Top-right corner: (r, c-1), (r, c), (r+1, c-1), (r+1, c)
- Bottom-left corner: (r-1, c), (r-1, c+1), (r, c), (r, c+1)
- Bottom-right corner: (r-1, c-1), (r-1, c), (r, c-1), (r, c)

If ANY of these 2x2 regions is entirely filled → cell is "thick"
"""
