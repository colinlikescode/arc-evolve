HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SEED-BASED VERTICAL STRIPE PROPAGATION        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-zero "seed" cell on the bottom row
• From the seed column, create a repeating stripe pattern extending to the RIGHT edge
• The pattern period is 2 columns: [seed_color, background]
• Each seed_color column extends VERTICALLY from bottom to top (full height)
• A secondary marker color appears at diagonal corner positions:
  - Top-left corners of each stripe segment (top row, column+1 from seed color)
  - Bottom-right corners of each stripe segment (bottom row)

CONCEPTUAL STRUCTURE:
• Starting from seed column position, fill every other column with the seed color (full height)
• The columns LEFT of the seed remain unchanged (background)
• Marker color appears where the top row meets column+1 of each stripe, and similar for bottom row

KEY INSIGHT:
The seed defines both the starting column AND the color for the stripe pattern.
"""
