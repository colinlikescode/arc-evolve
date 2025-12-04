HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PAIRED MARKERS DEFINE FILLED RECTANGLES       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each non-zero color appears exactly TWICE in the input (as a pair)
• The two cells of the same color define OPPOSITE CORNERS of a rectangle
• Fill the entire bounding rectangle between those two corners with that color

HOW TO IDENTIFY CORNERS:
• For each unique non-zero color, find both cell positions
• One cell defines (min_row, min_col) or similar corner
• The other cell defines the opposite corner
• The filled rectangle spans from min to max in both dimensions

PROCESS EACH COLOR INDEPENDENTLY:
• Group cells by color
• For each color pair: compute bounding box
• Fill that bounding box with the color
• Repeat for all colors

The background (zero) cells remain unchanged unless covered by a rectangle.
"""
