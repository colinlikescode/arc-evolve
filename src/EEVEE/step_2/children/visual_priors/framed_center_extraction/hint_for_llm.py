HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND THE FRAMED CENTER CELL                   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Search the input for a 3x3 rectangular FRAME pattern
• The frame consists of 8 border cells all of the SAME color (forming a ring)
• The CENTER cell of this 3x3 region contains a DIFFERENT color
• The output is a 1x1 grid containing ONLY that center color

WHAT TO LOOK FOR:
• A 3x3 region where all 8 surrounding cells share one color
• The middle cell has a distinct color from the frame
• Ignore scattered noise cells elsewhere in the grid

THE ANSWER:
• Extract the color value from the center of the framed region
• Output it as a single 1x1 cell
"""
