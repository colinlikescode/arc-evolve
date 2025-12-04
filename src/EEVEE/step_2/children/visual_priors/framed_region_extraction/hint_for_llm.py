HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT THE FRAMED RECTANGULAR REGION         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a rectangular region marked by a FRAME
• The frame has TWO distinct non-background colors:
  - One color marks the FOUR CORNERS of the rectangle
  - Another color forms VERTICAL EDGE LINES on left and right sides

HOW TO IDENTIFY THE REGION:
• Find two vertical lines of the same non-background color
• These lines should be connected at top and bottom by the corner color
• The corners appear where the vertical lines start and end

EXTRACTION:
• Identify the bounding box defined by the corner markers
• Extract the entire rectangular region including the frame
• Discard all content outside this bounded region
• Preserve everything inside (including any scattered cells within)

The scattered cells of the corner color OUTSIDE the frame are noise to be ignored.
"""
