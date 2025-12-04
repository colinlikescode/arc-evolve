HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NESTED L-SHAPE / STAIRCASE EXPANSION PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output is 2× the input size in each dimension
• The input contains nested rectangular/L-shaped color regions meeting at a corner
• Empty cells (zeros or the outermost dominant color) mark incomplete areas

HOW TO CONSTRUCT THE OUTPUT:
• Each color in the input occupies a "level" in the nesting hierarchy
• The innermost/smallest region color is level 0, expanding outward
• In the output, each color's region extends as a full row AND column band at its level
• The pattern forms diagonal staircase boundaries where each color extends to form complete L-shapes across the doubled grid

KEY INSIGHT:
• For each cell (r, c) in the output, determine which color "owns" that position
• A color at nesting level N extends from the corner to form bands of width equal to its original extent
• The innermost color fills the "base" everywhere except where outer colors claim territory
• Outer colors extend their horizontal and vertical spans to meet at diagonal boundaries
"""
