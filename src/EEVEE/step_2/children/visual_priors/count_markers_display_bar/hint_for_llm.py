HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A COUNT-AND-DISPLAY-AS-BAR PUZZLE     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• COUNT the total number of non-background cells in the input
• The POSITION of markers in input does NOT matter - only the COUNT
• OUTPUT: Display that count as a horizontal bar in a new color

BAR PLACEMENT RULES:
• Start filling from top-left corner (row 0, col 0)
• Fill leftward along the top row first
• If count exceeds grid width, overflow to the CENTER of the next row
• Continue this pattern for additional overflow

EXAMPLE LOGIC:
• 1 marker → fill 1 cell at top-left
• 2 markers → fill 2 cells in top row
• 3 markers → fill entire top row
• 4 markers → fill top row + center of row 2

YOUR APPROACH:
1. Count all non-zero cells in input
2. Create output grid filled with background
3. Place output color cells according to count using the bar pattern
"""
