HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL MIRROR + VERTICAL TILING PATTERN   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions: height = input_height × input_height, width = input_width × 2

STEP 1 - HORIZONTAL REFLECTION:
• For each row in the input, create a new row by concatenating:
  [row_reversed] + [row_original]
• This creates a horizontally symmetric row (mirror along center)

STEP 2 - VERTICAL TILING:
• Take the horizontally-mirrored pattern (same number of rows as input)
• Repeat/tile this pattern vertically input_height times
• Stack the pattern on top of itself to reach the final height

EXAMPLE STRUCTURE (3×2 input → 9×4 output):
Input row [A, B] → Output row [B, A, A, B]
The full mirrored pattern is then repeated 3 times vertically.

KEY INSIGHT:
• The non-zero color stays the same
• Zero (background) cells follow the same mirroring logic
• The pattern creates both horizontal AND vertical symmetry structures
"""
