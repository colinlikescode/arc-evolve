HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL EXPANSION FROM SINGLE MARKER         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-zero "marker" cell in the input
• Remove the marker (set to zero in output)
• Place four fixed colors at the four DIAGONAL positions around the marker:
  - Upper-left diagonal: one specific color
  - Upper-right diagonal: another specific color  
  - Lower-left diagonal: another specific color
  - Lower-right diagonal: another specific color

THE FOUR COLORS FORM A CONSISTENT 2x2 PATTERN:
• Top-left and top-right positions get one pair of colors
• Bottom-left and bottom-right positions get another pair of colors
• Identify which color goes where by examining training examples

BOUNDARY HANDLING:
• If a diagonal position would be outside the grid, simply don't place that color
• Only place colors at valid grid positions

YOUR APPROACH:
1. Locate the marker position (row, col)
2. For each of the four diagonal offsets: (-1,-1), (-1,+1), (+1,-1), (+1,+1)
3. If the resulting position is within bounds, place the corresponding color
4. Determine the four colors and their positions from training examples
"""
