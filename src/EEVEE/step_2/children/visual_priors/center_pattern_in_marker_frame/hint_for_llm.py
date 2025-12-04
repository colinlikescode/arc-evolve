HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CENTER PATTERN WITHIN CORNER MARKERS          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Four corner markers define a rectangular frame region
• A pattern (different non-background color) exists in the grid
• The pattern must be CENTERED horizontally within the column bounds of the corner markers
• Corner markers remain in their original positions

HOW TO SOLVE:
1. Find the 4 corner marker cells (they form a rectangle)
2. Identify the content region (rows and columns between markers)
3. Extract the pattern made of the other non-background color
4. Calculate the horizontal center of the marker frame
5. Reposition the pattern so it's horizontally centered within the frame
6. Keep corner markers fixed, clear areas outside the centered pattern

KEY INSIGHT:
• The pattern's horizontal span should be centered between the left and right marker columns
• Vertical positioning should place the pattern within the marker rows
"""
