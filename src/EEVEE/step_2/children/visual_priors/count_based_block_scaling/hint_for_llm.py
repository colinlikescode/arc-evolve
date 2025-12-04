HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SCALE FACTOR = COUNT OF NON-ZERO CELLS        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count all non-zero cells in the input → this is the SCALE FACTOR (N)
• Output dimensions = input dimensions × N
• Each cell in the input expands to an N×N block in the output
• Non-zero cells → N×N block filled with that cell's color
• Zero cells → N×N block of zeros (background)

STRUCTURE:
Input cell at (row, col) maps to output block at:
  rows: [row × N : row × N + N]
  cols: [col × N : col × N + N]

EXAMPLE LOGIC:
- If input has 2 non-zero cells → each cell becomes 2×2 block
- If input has 3 non-zero cells → each cell becomes 3×3 block
- If input has 5 non-zero cells → each cell becomes 5×5 block

The grid structure is preserved; only the scale changes based on non-zero count.
"""
