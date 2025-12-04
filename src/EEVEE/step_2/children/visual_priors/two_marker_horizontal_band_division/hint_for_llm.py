HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TWO-MARKER HORIZONTAL BAND DIVISION           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero cells (markers) in the input
• The marker with the SMALLER row index owns the TOP band
• The marker with the LARGER row index owns the BOTTOM band
• The boundary between bands is determined by the midpoint between the two markers

FOR EACH BAND:
• Fill the ENTIRE row of the marker with that marker's color
• Fill the FIRST and LAST rows of the band with that color
• Fill the LEFT and RIGHT edge columns (first and last) with that color
• Leave interior cells as background (zero)

VISUAL PATTERN:
Each band creates a "frame" effect where:
- Top edge row = filled
- Bottom edge row = filled  
- Left column = filled
- Right column = filled
- Marker's original row = filled
- All other interior = background

The grid is split roughly in half, with each marker defining its region's appearance.
"""
