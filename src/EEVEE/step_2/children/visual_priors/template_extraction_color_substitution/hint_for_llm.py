HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  TEMPLATE EXTRACTION WITH COLOR SUBSTITUTION             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains rectangular FRAMES outlined by a "frame color"
• A different "marker color" appears as scattered cells throughout the grid
• Find the LARGEST rectangular frame in the input
• Extract this frame's dimensions for the output

COLOR SUBSTITUTION:
• The frame outline becomes the MARKER color (not the original frame color)
• The interior starts as background (zeros)
• Any marker-colored cells that were INSIDE the template frame are preserved at their relative positions

WHAT TO DO:
1. Identify the frame color (forms rectangular borders)
2. Identify the marker color (scattered individual cells)
3. Find the largest frame and extract its bounding region
4. Create output with marker color as the new border
5. Copy any marker cells from inside the original frame to the output interior
"""
