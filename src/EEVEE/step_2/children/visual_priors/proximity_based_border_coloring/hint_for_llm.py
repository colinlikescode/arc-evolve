HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PROXIMITY-BASED BORDER COLORING PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two opposing borders exist (left/right OR top/bottom) with distinct colors
• Marker cells in the interior are replaced based on PROXIMITY
• Each marker takes the color of the NEAREST border

HOW TO DETERMINE PROXIMITY:
• For vertical borders (left/right columns): compare column distance to each border
• For horizontal borders (top/bottom rows): compare row distance to each border
• The marker adopts the color of whichever border is closer

WHAT TO DO:
1. Identify the two border colors and their positions (edges of the grid)
2. Find all marker cells (the third color in the interior)
3. For each marker, calculate distance to each border
4. Replace the marker with the color of the closer border
5. Keep the original borders unchanged
"""
