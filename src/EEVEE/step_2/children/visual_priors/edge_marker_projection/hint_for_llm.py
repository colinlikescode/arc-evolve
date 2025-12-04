HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EDGE MARKER PROJECTION PUZZLE                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There is a central rectangular BLOCK of uniform fill color
• Scattered around the grid are single-cell MARKERS (different colors)
• Each marker "projects" onto the edge of the block along its row or column

HOW PROJECTION WORKS:
• Markers to the LEFT of the block → project onto the LEFT edge of the block (same row)
• Markers to the RIGHT of the block → project onto the RIGHT edge of the block (same row)
• Markers ABOVE the block → project onto the TOP edge of the block (same column)
• Markers BELOW the block → project onto the BOTTOM edge of the block (same column)

THE OUTPUT:
• The block's edge cells are REPLACED with the marker's color where projections land
• Original markers remain in place
• Interior cells of the block stay unchanged
• All other cells remain as background

YOUR APPROACH:
1. Identify the rectangular block (contiguous region of non-background fill color)
2. Find all isolated marker pixels outside the block
3. For each marker, determine its projection direction (horizontal or vertical)
4. Replace the corresponding edge cell of the block with the marker's color
"""
