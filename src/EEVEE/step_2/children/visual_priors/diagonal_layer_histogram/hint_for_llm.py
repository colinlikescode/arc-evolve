HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL LAYER TO STAIRCASE HISTOGRAM         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains colored regions arranged as diagonal layers from a corner
• Each distinct color forms a "layer" at a certain depth from the edge
• Extract the unique colors in order from the corner outward (following the diagonal)

OUTPUT CONSTRUCTION:
• Output width = number of distinct non-background colors
• Output height = sum of unique layer depths (or max extent needed)
• Each column represents one color, ordered by layer (outermost first)
• Column height = how many cells that color extends in its layer direction
• Fill from bottom with the color, zeros (background) above

VISUAL PATTERN:
• The output looks like a staircase descending from left to right
• First column is tallest (the color spanning the full edge)
• Each subsequent column is shorter (deeper layers have less extent)
• Think of it as "unfolding" the diagonal layers into vertical bars

KEY INSIGHT:
• Trace the diagonal from corner → find colors in order → measure each layer's extent → create histogram columns
"""
