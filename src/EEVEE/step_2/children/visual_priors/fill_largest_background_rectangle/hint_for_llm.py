HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL THE LARGEST RECTANGULAR BACKGROUND HOLE  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Scan the grid to find all possible rectangular regions that contain ONLY background (zero) cells
• Identify the largest such rectangle by area (height × width)
• Fill that entire rectangle with a new marker color
• Leave all other cells unchanged

KEY OBSERVATIONS:
• The marker color used for filling is NOT present in the input
• Only ONE rectangle gets filled (the largest one)
• The rectangle must be entirely composed of background cells
• If there's a tie in area, check for position preference (e.g., leftmost, topmost)

YOUR APPROACH:
1. Identify the background color (typically zero)
2. Find all maximal rectangles containing only background cells
3. Select the rectangle with the largest area
4. Fill that rectangle with the marker color
5. Keep everything else unchanged
"""
