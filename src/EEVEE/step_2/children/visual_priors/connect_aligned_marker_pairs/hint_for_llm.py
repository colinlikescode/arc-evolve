HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECT ALIGNED MARKER PAIRS WITH FILL LINES  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all non-background marker cells in the grid
• Identify pairs of markers that share the SAME ROW or SAME COLUMN
• For each aligned pair: fill all cells BETWEEN them with a secondary fill color
• The marker cells themselves remain unchanged
• Markers without a partner in their row/column stay isolated (no fill)

KEY OBSERVATIONS:
• Only pairs aligned horizontally OR vertically get connected
• The fill color is different from the marker color
• Cells between markers are filled; the markers act as endpoints
• If a marker has no aligned partner, nothing changes around it

YOUR CODE MUST:
1. Locate all marker cells (non-background)
2. Group markers by row and by column
3. For each row/column with exactly 2 markers: fill the cells between them
4. Preserve the original marker positions
"""
