HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECT ALIGNED MARKERS WITH LINES            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all non-zero marker cells in the input
• For each pair of markers on the SAME ROW: draw a horizontal line between them
• For each pair of markers on the SAME COLUMN: draw a vertical line between them
• Lines fill all cells between the two markers (inclusive) with the marker color
• Markers not aligned with any other marker remain as single points

KEY INSIGHT:
• Look for markers sharing rows → connect horizontally
• Look for markers sharing columns → connect vertically
• The original markers are preserved; only the gaps are filled

YOUR APPROACH:
1. Identify all non-zero cell positions
2. Group markers by row and by column
3. For each row/column with 2+ markers, fill the span between the leftmost/topmost and rightmost/bottommost markers
"""
