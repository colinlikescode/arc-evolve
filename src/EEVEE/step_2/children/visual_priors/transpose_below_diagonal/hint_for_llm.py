HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TRANSPOSE OFF-DIAGONAL ELEMENTS               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The main diagonal (where row == col) contains a fixed marker color - KEEP IT
• All colored cells BELOW the diagonal get REFLECTED to ABOVE the diagonal
• The reflection maps position (row, col) → (col, row)
• After reflection, cells below the diagonal become background (zero)

CONCEPTUALLY:
• Input has data below diagonal, output has data above diagonal
• The diagonal itself remains unchanged
• Each non-background cell at (r, c) where r > c moves to (c, r)

WHAT YOUR CODE MUST DO:
1. Identify the background color (typically zero) and diagonal marker color
2. For each cell (row, col) where row > col (below diagonal):
   - If it's not background, copy it to (col, row) in the output
3. Keep the diagonal intact
4. Fill everything below the diagonal with background color
"""
