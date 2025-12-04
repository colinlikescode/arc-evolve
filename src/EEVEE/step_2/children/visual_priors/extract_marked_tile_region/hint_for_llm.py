HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT MARKED REGION FROM TILED PATTERN     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a repeating tile pattern with separator lines
• ONE rectangular region has its separator lines replaced with a DIFFERENT "marker" color
• Find the rectangular boundary formed by this marker color
• Extract the region INCLUDING the marker border

HOW TO IDENTIFY THE MARKED REGION:
• Look for a color that appears in a rectangular frame pattern
• This color differs from the regular separator/grid line color
• The marker color forms complete horizontal and vertical lines bounding a region

OUTPUT CONSTRUCTION:
• Extract the rectangular region bounded by the marker color
• Include the marker color as the border of the output
• The interior contains the tile pattern from within that marked region
"""
