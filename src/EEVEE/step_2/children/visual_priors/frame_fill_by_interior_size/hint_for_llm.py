HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME INTERIOR FILL BY SIZE RANKING          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all closed rectangular frames (borders made of non-background color)
• Calculate the INTERIOR AREA of each frame (width × height of hollow region)
• Rank the frames by interior area from SMALLEST to LARGEST
• Fill each frame's interior with a color based on its size rank:
  - LARGEST interior area → one fill color
  - SMALLER interior areas → another fill color

WHAT TO IDENTIFY:
• Frames are rectangular outlines with hollow interiors
• The border cells remain unchanged
• Only the interior (background) cells get filled
• The fill color assignment is based on relative size comparison among all frames

KEY INSIGHT:
The largest frame(s) by interior area receive one fill color, while smaller frames receive a different fill color. Count interior cells (excluding the border) to determine size ranking.
"""
