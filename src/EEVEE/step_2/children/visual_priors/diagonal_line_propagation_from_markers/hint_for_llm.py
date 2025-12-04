HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL LINE PROPAGATION FROM MARKERS        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains rectangular regions filled with different colors
• Find MARKER CELLS: isolated cells with a unique color within their region
• From each marker, draw DIAGONAL LINES extending in BOTH diagonal directions
• Lines extend like an "X" pattern: one line going ↗↙ and another going ↘↖

HOW TO APPLY:
1. Identify marker cells (cells whose color differs from their local region)
2. For each marker at position (r, c):
   - Draw the marker's color along the diagonal (r+k, c+k) for all valid k
   - Draw the marker's color along the anti-diagonal (r+k, c-k) for all valid k
   - Both positive and negative k values (extending in both directions)
3. Keep the original grid structure, only modifying cells along the diagonals

The diagonals continue until they reach grid boundaries, crossing through all regions they encounter.
"""
