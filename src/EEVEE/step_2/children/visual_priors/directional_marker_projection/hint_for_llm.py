HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DIRECTIONAL MARKER PROJECTION       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the small cluster of the "marker" color (the rare third color)
• Determine the DIRECTION the marker shape indicates:
  - Horizontal line → extend left/right
  - Vertical line → extend up/down  
  - Diagonal/L-shape → extend diagonally
• Project/extend the marker pattern along that direction
• The marker color REPLACES only ONE of the two background colors
• The other background color acts as a "wall" that blocks extension

KEY INSIGHT:
• The marker shape's orientation defines the projection axis
• Each cell of the marker extends as a "ray" in the indicated direction
• Extension continues to the grid boundary, but only overwrites the "empty" background color

YOUR APPROACH:
1. Identify the three colors: two backgrounds, one marker
2. Find the marker cluster and determine its directional orientation
3. For each marker cell, project along that direction
4. Replace only the appropriate background color with marker color
"""
