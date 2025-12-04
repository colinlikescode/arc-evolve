HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ROW-BASED TILING BY NON-ZERO CELL COUNT       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• For each row in the input, count how many non-zero cells it contains
• The output is a grid of input-sized blocks
• Output dimensions: (input_height × total_non_zero_cells) × (input_width × total_non_zero_cells)
• For each row R in the input with K non-zero cells:
  - Tile the ENTIRE input pattern horizontally K times starting at block-row R
• Rows with zero non-zero cells contribute only background (zeros)

KEY INSIGHT:
• Count total non-zero cells in the input = N
• Output size = (input_height × N) × (input_width × N)
• Each row's horizontal tiling count = number of non-zero cells in that row
• Vertical position corresponds to original row position (scaled by input height)

STRUCTURE:
• The pattern creates a "staircase" or "L-shaped" filled region
• Non-zero rows get copies of the full input tiled horizontally
• The rest of the output is filled with the background color (zeros)
"""
