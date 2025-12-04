HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL LINE + BOTTOM ROW FILL PATTERN       ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• A vertical stripe of non-zero color along one edge (e.g., left column)
• The remaining cells are background (zeros)
• The grid is square (N×N)

THE TRANSFORMATION RULE:
1. KEEP the original vertical stripe unchanged
2. DRAW an anti-diagonal line using a FIRST new color:
   - Starts at top-right corner (row 0, last column)
   - Goes diagonally down-left (row+1, col-1 each step)
   - Stops when it reaches the column adjacent to the vertical stripe
3. FILL the bottom row (excluding the vertical stripe column) with a SECOND new color

VISUAL PATTERN:
```
[stripe] [0] [0] [0] [diagonal]     ← diagonal at top-right
[stripe] [0] [0] [diagonal] [0]
[stripe] [0] [diagonal] [0] [0]
[stripe] [diagonal] [0] [0] [0]     ← diagonal reaches bottom
[stripe] [fill] [fill] [fill] [fill] ← bottom row filled
```

The diagonal and fill colors are consistent NEW colors (not the stripe color).
"""
