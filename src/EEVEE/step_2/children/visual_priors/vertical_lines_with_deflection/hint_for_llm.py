HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL LINES DEFLECTED BY MARKERS          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A designated row (e.g., bottom row) contains "source markers" at certain columns
• Scattered "deflector" cells exist elsewhere in the grid
• Draw vertical lines upward from each source marker column
• Each deflector cell affects the nearest vertical line in its zone
• When a line reaches a deflector's row, it SHIFTS one column toward the deflector
• From that row upward, the line continues at the new column position
• The deflector cells are preserved in the output

KEY OBSERVATIONS:
• Lines extend the full height of the grid
• Deflection happens AT the row of the deflector cell
• The line shifts toward the deflector (left or right by one column)
• After deflection, the line continues straight at the new position

YOUR CODE MUST:
1. Identify source markers in the designated row
2. Identify deflector cells in the grid
3. For each source marker, draw a vertical line that deflects when encountering its associated deflector
4. Preserve the deflector cells in the output
"""
