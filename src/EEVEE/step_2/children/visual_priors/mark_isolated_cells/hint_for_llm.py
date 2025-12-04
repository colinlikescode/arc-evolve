HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS PUZZLE MARKS ISOLATED/LONELY CELLS       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the dominant non-zero color in the grid
• For each cell of that dominant color, check its 4 orthogonal neighbors (up, down, left, right)
• If a cell has ZERO neighbors of the same dominant color, it is "isolated"
• Change all isolated cells to a marker color (a different non-zero color)
• All other cells remain unchanged

WHAT MAKES A CELL "ISOLATED":
• It must be the dominant color
• None of its 4 adjacent cells (not diagonals) share that same color
• It stands alone, not connected to any cluster

YOUR APPROACH:
1. Identify the dominant non-zero color (most frequent)
2. Identify the marker color (will be used for isolated cells)
3. For each cell of the dominant color, count same-color orthogonal neighbors
4. If count == 0, change that cell to the marker color
"""
