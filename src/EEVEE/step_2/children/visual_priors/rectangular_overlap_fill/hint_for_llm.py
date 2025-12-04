HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RECTANGULAR REGION OVERLAP FILLING            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input has TWO distinct colored rectangular regions on a background
• Find the ROW RANGE each rectangle spans
• Find the COLUMN RANGE each rectangle spans
• The OVERLAP region is where:
  - Rows are covered by BOTH rectangles (intersection of row ranges)
  - Columns are covered by BOTH rectangles (intersection of column ranges)
• Fill this overlap region with a FILL COLOR (typically a consistent marker color)
• Only fill cells that were originally BACKGROUND (don't overwrite existing colors)

CONCEPTUALLY:
• Project each rectangle's rows and columns onto the grid
• Where both projections intersect AND the cell is background → fill with new color
• The fill creates a "bridge" or "connection" in the gap between the two rectangles

YOUR APPROACH:
1. Identify the two colored rectangular regions (non-background)
2. Compute row range and column range for each
3. Find intersection of row ranges AND intersection of column ranges
4. Fill background cells in that intersection with the fill color
"""
