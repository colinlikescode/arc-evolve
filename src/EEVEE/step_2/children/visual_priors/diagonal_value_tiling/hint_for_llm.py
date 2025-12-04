HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL-VALUE BASED TILING PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output size = input dimensions × input dimensions (e.g., 3×3 → 9×9)
• Identify the "key value" - the value on the main diagonal of the input
• The output is a grid of blocks, each block sized like the input
• For each cell (row, col) in the input:
  - If input[row][col] == key_value: place the ENTIRE input pattern in that output block
  - Otherwise: fill that block with zeros

KEY INSIGHT:
• The main diagonal cells (0,0), (1,1), (2,2)... share the same value
• This diagonal value acts as a "marker" for where to tile the pattern
• Every position in the input matching this marker gets a copy of the full input

STRUCTURE:
Input position → Output block position
If input[r][c] == diagonal_value → copy input to block (r, c)
If input[r][c] != diagonal_value → block (r, c) is all zeros
"""
