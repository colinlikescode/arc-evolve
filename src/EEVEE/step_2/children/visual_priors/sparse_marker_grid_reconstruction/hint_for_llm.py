HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID LINE RECONSTRUCTION FROM SPARSE MARKERS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:

1. FIND THE FILLED RECTANGLE:
   • Locate a rectangular region dominated by one color (the "background/fill color")
   • This region stands out from the surrounding noise

2. IDENTIFY MARKER CELLS:
   • Within this rectangle, find sparse cells of a DIFFERENT color (the "line color")
   • These markers are NOT random - they indicate grid line positions

3. RECONSTRUCT THE PATTERN:
   • Each marker cell indicates that its ENTIRE row AND column should be the line color
   • Project marker positions to create horizontal and vertical lines
   • Fill remaining cells with the background/fill color

4. OUTPUT SIZE:
   • The output dimensions match the filled rectangle's dimensions
   • Output contains only two colors: the fill color and the line/marker color

THINK OF IT AS: The markers are "samples" from a hidden grid pattern - reconstruct the full grid by extending each marker into complete row and column lines.
"""
