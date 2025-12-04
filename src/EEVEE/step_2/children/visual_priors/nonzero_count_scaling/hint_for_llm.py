HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CELL SCALING BY NON-ZERO COUNT               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count the number of NON-ZERO cells in the input → this is your scale factor N
• Output dimensions = input_height × N, input_width × N
• Each cell (r, c) in the input becomes an N×N block in the output
• The block's position: rows [r×N : (r+1)×N], cols [c×N : (c+1)×N]
• The block is filled uniformly with the value from input[r][c]

KEY INSIGHT:
The scale factor is NOT fixed - it depends on how many non-zero cells exist.
- 4 non-zero cells → each cell becomes 2×2 block (output is 2× larger)
- 5 non-zero cells → each cell becomes... (wait, check examples)
- Actually: scale = count of non-zero cells in input

VISUAL PATTERN:
Input cell → N×N block of same color
Zero cell → N×N block of zeros
"""
