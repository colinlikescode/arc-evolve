HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LINE FILL BETWEEN ENDPOINT PAIRS              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find rows that have exactly two non-zero cells at opposite edges
• The left endpoint color expands rightward from the left edge
• The right endpoint color expands leftward from the right edge
• They meet at the CENTER of the row
• A special marker color is placed at the exact midpoint where they meet

KEY OBSERVATIONS:
• Each color fills approximately HALF the row
• The midpoint gets a distinct separator color (consistent across all filled rows)
• Rows without endpoint pairs remain unchanged
• The original endpoint positions keep their colors

YOUR APPROACH:
1. Identify rows with non-zero cells at both the leftmost and rightmost positions
2. For each such row, fill from left edge toward center with the left color
3. Fill from right edge toward center with the right color
4. Place the separator/marker color at the middle column
"""
