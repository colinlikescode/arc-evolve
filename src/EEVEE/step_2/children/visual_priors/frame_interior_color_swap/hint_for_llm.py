HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A FRAME-INTERIOR COLOR SWAP PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the rectangular region containing non-background colors
• This region has TWO distinct colors: a FRAME color and an INTERIOR color
• The frame color forms the outer border of the rectangle
• The interior color fills the center area

OUTPUT CONSTRUCTION:
• Extract/crop just the rectangular region (remove background)
• SWAP the two colors:
  - Where the frame color was → use the interior color
  - Where the interior color was → use the frame color

WHAT TO IDENTIFY:
1. The background color (most common, typically zero)
2. The bounding box of the non-background region
3. Which color is the "frame" (appears on edges)
4. Which color is the "interior" (appears in center)
5. Swap these two colors in the cropped output
"""
