HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A RECTANGLE HOLLOWING PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all solid rectangular regions of non-background colors
• For each rectangle: keep only the 1-cell-thick OUTER BORDER in the original color
• Fill the INTERIOR cells with a uniform "fill color" (same for all rectangles)

CONCEPTUALLY:
• Input rectangles are SOLID blocks
• Output rectangles are FRAMES/BORDERS with filled interiors
• Border = outermost row/column on each side of the rectangle
• Interior = everything inside the border (at least 1 cell inward from each edge)

YOUR CODE MUST:
1. Identify each distinct rectangular region by its color
2. Determine the bounding box of each rectangle
3. Keep the perimeter cells as the original color
4. Replace all interior cells (not on the perimeter) with the fill color
"""
