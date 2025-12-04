HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CROSS INTERSECTION HIGHLIGHT PUZZLE ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has TWO perpendicular lines crossing the grid:
  - One VERTICAL line (single column of non-background color)
  - One HORIZONTAL line (single row of different non-background color)
• These lines INTERSECT at exactly one cell

YOUR TASK:
1. Find the intersection point where the two lines cross
2. Create a 3×3 highlight region CENTERED on that intersection
3. Fill the 8 cells SURROUNDING the intersection with a new highlight color
4. The intersection cell itself KEEPS its original color (from one of the lines)
5. Only replace BACKGROUND cells in this 3×3 region; preserve the original line colors where they exist

THE HIGHLIGHT:
• Forms a 3×3 square around the intersection
• Uses a consistent marker color (not present in input)
• The original crossing lines remain visible through the highlight
"""
