HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL PATTERN INSIDE MARKER BOUNDARY          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has a background pattern with two colors (background + primary pattern color)
• A MARKER COLOR defines a rectangular bounded region
• Inside this region, cells have either the marker color OR the primary pattern color

YOUR TASK:
1. Identify the marker color (appears in a bounded rectangular region)
2. Find the bounding box of all marker-colored cells
3. Within that region: cells with the PRIMARY pattern color → change to FILL color
4. Marker color cells remain as marker color
5. Everything outside the bounded region stays unchanged

KEY INSIGHT:
• The marker acts as a "frame" - it stays unchanged
• Only the pattern color INSIDE the frame gets recolored
• The fill color is a new color not present in the original pattern
"""
