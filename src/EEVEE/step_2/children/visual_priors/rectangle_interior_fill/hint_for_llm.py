HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A RECTANGLE INTERIOR FILLING PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all solid rectangular regions of a non-background color
• For each rectangle, keep the 1-cell border in the original color
• Fill the interior (all cells not on the outer edge) with a new fill color

CONCEPTUAL APPROACH:
• Identify connected rectangular regions of the primary non-background color
• For each rectangle with bounding box (top, left, bottom, right):
  - Keep cells on the perimeter (top row, bottom row, left column, right column)
  - Change interior cells (row > top AND row < bottom AND col > left AND col < right) to fill color
• Rectangles that are too thin (width or height ≤ 2) may have no interior to fill

KEY INSIGHT:
• The border remains the original color
• Only the "inside" gets the new color
• This creates a hollow rectangle effect with filled interior
"""
