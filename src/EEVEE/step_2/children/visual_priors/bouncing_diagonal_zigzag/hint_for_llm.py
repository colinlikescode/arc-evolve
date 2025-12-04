HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BOUNCING DIAGONAL PATTERN           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the non-zero marker cell - this indicates the starting column position
• Fill the entire output grid with a secondary fill color
• Draw a diagonal that bounces off left and right edges

HOW THE BOUNCING WORKS:
• Start at the marker's column position in the bottom row
• Move upward through rows, shifting the diagonal position
• When the diagonal hits column 0, reverse direction (go right)
• When the diagonal hits the last column, reverse direction (go left)
• This creates a zigzag pattern with period = 2 × (width - 1)

VISUAL CONCEPT (for width 4):
Row 9: marker at col 0, moving right
Row 8: col 1
Row 7: col 2  
Row 6: col 3 (hit right edge, reverse)
Row 5: col 2
Row 4: col 1
Row 3: col 0 (hit left edge, reverse)
... pattern repeats

The marker color appears at exactly ONE position per row, tracing this bouncing path.
"""
