HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SELF-SIMILAR FRACTAL TILING PUZZLE  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = input dimensions × input dimensions (e.g., 3×3 → 9×9)
• The output is a grid of blocks, each block is the same size as the input
• For each cell (row, col) in the input:
  - If input[row][col] is NON-ZERO: place the ENTIRE input pattern in that block
  - If input[row][col] is ZERO: place a block of all zeros (background)

CONCEPTUAL STRUCTURE:
The input acts as BOTH the pattern AND the template for where to place copies.

Input:          Output structure:
0 X X           [zeros] [input] [input]
X X X     →     [input] [input] [input]
0 X X           [zeros] [input] [input]

KEY INSIGHT:
Each non-zero cell becomes a "stamp" location where the entire input is copied.
Each zero cell becomes an empty block filled with zeros.
"""
