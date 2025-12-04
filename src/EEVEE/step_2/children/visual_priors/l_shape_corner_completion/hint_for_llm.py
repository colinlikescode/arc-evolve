HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: L-SHAPE CORNER COMPLETION PUZZLE              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all L-shaped patterns (3 connected cells of the same non-zero color)
• Each L-shape occupies 3 corners of an implicit 2x2 square
• Place a MARKER COLOR at the 4th (missing) corner of each L-shape

HOW TO IDENTIFY THE MISSING CORNER:
• An L-shape has exactly 3 cells forming an "L" in any rotation
• Find the 2x2 bounding region that contains these 3 cells
• The empty cell in that 2x2 region is where the marker goes

VISUAL EXAMPLE:
```
X X      X X
  X  →   1 X   (marker fills the missing corner)
```

YOUR APPROACH:
1. Identify all connected components of the non-zero color
2. For each 3-cell L-shaped component, find its 2x2 bounding box
3. Place the marker color at the one empty position in that 2x2 box
"""
