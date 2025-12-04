HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL X-RAY EXPANSION FROM SINGLE POINT    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-zero cell in the input at position (row, col)
• Draw TWO diagonal lines through this point using the same color:
  - Main diagonal (↘↖): cells where row - col = constant
  - Anti-diagonal (↗↙): cells where row + col = constant

CONCEPTUALLY:
• The point "emits" rays in all four diagonal directions
• Each ray continues until it hits a grid boundary
• This creates an X pattern centered on the original point

KEY INSIGHT:
• For the main diagonal direction: move (row±k, col±k) for all valid k
• For the anti-diagonal direction: move (row±k, col∓k) for all valid k
• Keep the original point colored
• Only color cells that are within grid bounds
"""
