HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CONCENTRIC SPIRAL MAZE PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input is a uniform grid of background color
• Output draws nested rectangular rings spiraling inward
• The spiral starts at the TOP edge going RIGHT
• Alternates between a fill color and background color every 2 units

THE SPIRAL PATTERN:
• Row 0: fill color (going right)
• Row 1: background color (going left, except last column)
• Row 2: fill color (going right, except last 2 columns)
• Continue alternating inward...

KEY INSIGHT:
• Think of it as drawing a rectangular spiral path
• The path width is 1 cell, walls between paths are 1 cell
• Start top-left corner, spiral clockwise inward
• Color the path with fill color, leave walls as background

CONCEPTUAL APPROACH:
• For each cell (r, c), determine its "distance" from the nearest edge
• Use this distance to determine which ring the cell belongs to
• Alternate colors based on the ring number and position within the spiral
"""
