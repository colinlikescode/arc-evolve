HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ALTERNATING DIAGONAL TRIANGLE FILL PATTERN    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a repeating diagonal stripe pattern (marker color on background)
• The diagonals divide the grid into triangular regions
• View the grid as repeating "tiles" - each tile spans from one diagonal to the next
• Fill the LOWER-LEFT triangular regions with a NEW color, but in an ALTERNATING pattern

HOW TO IDENTIFY REGIONS TO FILL:
• Track the tile/segment index as you move horizontally
• In alternating tiles (e.g., odd-indexed), fill the triangular region BELOW/LEFT of the diagonal
• The triangular region consists of cells where (row_index > col_index within the tile)
• Keep the diagonal markers unchanged; only modify background cells

PATTERN:
• Tile 0: no fill
• Tile 1: fill lower-left triangle  
• Tile 2: no fill
• Tile 3: fill lower-left triangle
• (continues alternating...)

The new fill color is distinct from both background and the diagonal marker color.
"""
