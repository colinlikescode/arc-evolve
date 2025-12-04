HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL EXTENSION WITH OFFSET MARKERS        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a diagonal line of a "primary" color
• A triangular "marker" region (different color) indicates offset distances
• The marker region shows where parallel copies of the diagonal should appear

WHAT TO DO:
1. Identify the diagonal line (non-background, non-marker color)
2. Find the marker region (typically triangular, adjacent to diagonal)
3. The marker region indicates the OFFSET for parallel diagonal copies
4. Remove all marker cells
5. Extend the original diagonal to fill the grid
6. Create parallel diagonal copies offset by the marker region's extent

KEY INSIGHT:
• Each row of marker cells indicates a parallel diagonal should pass through that region
• The diagonal pattern repeats with spacing determined by the marker width
• The output contains only the background and the diagonal color (marker removed)
"""
