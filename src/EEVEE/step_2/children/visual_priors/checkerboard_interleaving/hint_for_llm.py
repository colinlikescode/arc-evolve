HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CHECKERBOARD INTERLEAVING PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input: Two rows, each filled with a single uniform color (call them Color A and Color B)
• Output: Same dimensions, but colors are interleaved in a checkerboard pattern

THE CHECKERBOARD PATTERN:
• For each cell at position (row, col):
  - If (row + col) is EVEN: use the color from the FIRST input row (Color A)
  - If (row + col) is ODD: use the color from the SECOND input row (Color B)

VISUAL PATTERN:
Row 0: A B A B A B ...
Row 1: B A B A B A ...

KEY INSIGHT:
• The two solid horizontal stripes become an alternating checkerboard
• Adjacent cells (up/down/left/right) always have opposite colors
"""
