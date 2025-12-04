HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BLOCK PRESENCE → SUMMARY GRID MAPPING         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains 2x2 blocks of a non-background color at various positions
• The output is a fixed-size summary grid (3x3)
• Divide the input into a conceptual grid of regions matching the output size
• For each region: if a 2x2 block is present → mark with indicator color
• For each region: if no block present → leave as background

KEY INSIGHT:
• Find all 2x2 blocks of the non-background color in the input
• Map each block's position to which "zone" of the input it falls in
• The zones correspond to cells in a 3x3 output grid
• Mark output cells where blocks exist, leave others as background

SPATIAL MAPPING:
• Top-left region of input → top-left of output
• Center region of input → center of output
• And so on for all 9 regions in a 3x3 arrangement

The output essentially answers: "Which zones contain a colored block?"
"""
