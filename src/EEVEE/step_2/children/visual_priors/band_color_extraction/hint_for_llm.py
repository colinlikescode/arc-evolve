HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL/HORIZONTAL BAND COLOR EXTRACTION     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid contains distinct colored bands arranged spatially (left-to-right or top-to-bottom)
• Each band has a dominant color, though boundaries between bands are irregular/noisy
• The output extracts the unique band colors in their spatial order

HOW TO IDENTIFY BANDS:
• Look for the dominant color in each vertical (or horizontal) region
• Bands are ordered from left→right (vertical bands) or top→bottom (horizontal bands)
• The number of distinct colors = number of bands = output size

OUTPUT FORMAT:
• For vertical bands: output is 1 row × N columns (colors left to right)
• For horizontal bands: output is N rows × 1 column (colors top to bottom)
• Each cell contains one band's dominant color in spatial order

YOUR APPROACH:
1. Identify the distinct colors present in the grid
2. Determine if bands are vertical or horizontal based on color distribution
3. Find the spatial ordering of colors (which appears first/leftmost or topmost)
4. Output colors in that spatial order as a single row or column
"""
