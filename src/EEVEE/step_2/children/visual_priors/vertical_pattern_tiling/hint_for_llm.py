HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A VERTICAL PATTERN TILING PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a small repeating unit (a few rows of non-zero cells)
• This unit pattern tiles/repeats vertically to fill the entire output grid
• The output has the SAME dimensions as the input

HOW TO IDENTIFY THE TILE:
• Find the consecutive rows containing non-zero cells
• This forms your "tile" or "repeating unit"
• The tile height = number of rows in this unit

HOW TO GENERATE OUTPUT:
• Take the identified tile (the non-zero row pattern)
• Repeat it vertically starting from row 0
• Continue until the entire grid height is filled
• Use modular arithmetic: output[row] = tile[row % tile_height]

KEY INSIGHT:
The pattern wraps around - if your tile is N rows tall, row indices cycle through 0, 1, ..., N-1, 0, 1, ... etc.
"""
