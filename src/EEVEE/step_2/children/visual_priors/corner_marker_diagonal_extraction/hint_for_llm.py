HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CORNER MARKER EXTRACTION WITH DIAGONAL FLIP   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the rectangular FRAME (border made of a single non-background color)
• Identify the 4 CORNER MARKERS inside the frame (non-zero, non-frame colored cells)
• Each marker gets REMOVED from inside and PLACED OUTSIDE the frame

DIAGONAL REFLECTION PATTERN:
• Top-left inner marker → Bottom-right outer corner (beyond frame)
• Top-right inner marker → Bottom-left outer corner (beyond frame)
• Bottom-left inner marker → Top-right outer corner (beyond frame)
• Bottom-right inner marker → Top-left outer corner (beyond frame)

POSITIONING:
• External markers are placed ONE cell diagonally outward from the frame corners
• The frame remains intact but its interior is cleared (becomes background)

KEY INSIGHT: Each marker "escapes" to the OPPOSITE external corner, reflected through the center of the frame.
"""
