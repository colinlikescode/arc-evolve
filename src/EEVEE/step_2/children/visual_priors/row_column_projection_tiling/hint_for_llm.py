HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ROW/COLUMN PROJECTION WITH 2×2 TILING         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = 2 × input dimensions (both height and width)
• The input is tiled 2×2 to create the output structure
• Within each tile, apply the PROJECTION FILL rule:

PROJECTION FILL RULE:
• For each cell (r, c) in the input:
  - If input[r][c] is non-zero: keep it as-is in the output tile
  - If input[r][c] is zero BUT row r OR column c contains any non-zero cell: 
    replace with a SECONDARY FILL color
  - If input[r][c] is zero AND neither row r nor column c has non-zero cells:
    keep it as zero/background

IDENTIFYING THE SECONDARY FILL COLOR:
• Look for a color that appears in the output but NOT in the input
• This is the "projection shadow" color

YOUR CODE MUST:
1. Identify which rows and columns contain non-zero cells
2. Create the projection mask (cells where row OR column has color)
3. Tile this modified pattern 2×2 to create the output
"""
