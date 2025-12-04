HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME WITH SCALED PATTERN FILL                ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• INPUT has TWO components:
  1. A hollow rectangular FRAME (border color)
  2. A small PATTERN elsewhere (fill color)

• OUTPUT construction:
  1. Extract the frame (including its border)
  2. Determine the interior dimensions (frame minus border)
  3. Scale up the small pattern to fill the interior
  4. The scale factor = interior_size ÷ pattern_size (per dimension)
  5. Each cell in the small pattern becomes a block of cells in the output

SCALING LOGIC:
• For each cell in the small pattern:
  - If non-zero: fill corresponding block with that color
  - If zero (background): leave that block as background
• The frame border remains intact around the scaled pattern

KEY OBSERVATIONS:
• The frame defines the output size
• The pattern defines what fills the interior
• Pattern is scaled uniformly to match interior dimensions
"""
