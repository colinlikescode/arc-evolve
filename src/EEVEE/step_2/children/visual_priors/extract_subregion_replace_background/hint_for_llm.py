HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT PATTERN & REPLACE BACKGROUND WITH 0   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
1. Identify the BACKGROUND COLOR (the most common/dominant color filling the grid)
2. Find all cells that are NOT the background color
3. Compute the BOUNDING BOX around all non-background cells
4. Extract that rectangular region from the input
5. In the extracted region, REPLACE any background-colored cells with 0 (black)

KEY INSIGHT:
• Non-background colors stay as they are
• Background color WITHIN the bounding box → becomes 0
• This reveals the "true shape" of the embedded pattern with gaps shown as black

YOUR APPROACH:
• First determine which color is the background (most frequent)
• Find min/max row and column of non-background cells
• Crop to that bounding box
• Map: background → 0, other colors → unchanged
"""
