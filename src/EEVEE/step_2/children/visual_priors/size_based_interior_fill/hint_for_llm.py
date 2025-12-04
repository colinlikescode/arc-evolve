HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SIZE-BASED INTERIOR FILL TRANSFORMATION       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all solid rectangular regions of the same non-background color
• Compare their sizes (total area = width × height)
• For each rectangle:
  - Keep the OUTER BORDER (1 cell thick) in the original color
  - Fill the INTERIOR with a new color based on size ranking

SIZE → COLOR MAPPING:
• The LARGER rectangle gets one specific fill color for its interior
• The SMALLER rectangle gets a different fill color for its interior

WHAT TO DO:
1. Identify all rectangular regions of the primary non-background color
2. Calculate the area of each rectangle
3. Rank rectangles by size
4. For each rectangle: preserve the 1-cell border, fill interior based on size rank
   - Larger → one fill color
   - Smaller → another fill color

The border remains unchanged; only the interior (cells not on the edge) gets recolored.
"""
