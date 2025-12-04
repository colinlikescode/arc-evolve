HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COPY PATTERN TO MARKER LOCATION               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains TWO key elements:
  1. A multi-cell PATTERN (connected or nearby colored cells)
  2. A single isolated MARKER cell (different color, stands alone)

• The marker indicates WHERE to copy the pattern
• The pattern is copied so that its "anchor point" aligns with the marker position
• The anchor point is typically where the pattern would have a cell at the marker's relative position

WHAT TO DO:
1. Identify the marker cell (isolated single cell, often a unique color)
2. Identify the main pattern (group of non-background, non-marker cells)
3. Determine the pattern's bounding box and relative structure
4. Copy the pattern to the marker location, aligning appropriately
5. Remove the marker cell (it gets replaced by the pattern)
6. Keep the original pattern in place

NOTE: The pattern's position relative to the marker determines the exact placement - the copied pattern is positioned so the marker location becomes part of or adjacent to the copied pattern.
"""
