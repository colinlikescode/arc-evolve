HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BLOCK REGION SUMMARIZATION PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a grid of solid-colored rectangular REGIONS
• Each region is filled with a single uniform color
• Regions are arranged in a grid layout (R rows × C columns of blocks)
• The output is a small R × C grid

HOW TO SOLVE:
1. Identify the background color (usually the color forming the border/padding)
2. Find the bounding box of all non-background content
3. Detect the grid structure: how many block-rows and block-columns exist
4. For each block position, sample ONE cell to get that region's color
5. Build the output grid where output[r][c] = color of the block at row r, column c

KEY INSIGHT:
• The output is essentially a "thumbnail" or "summary" of the input
• Each large uniform region becomes exactly one pixel
• Spatial relationships are preserved - top-left block → top-left output cell
"""
