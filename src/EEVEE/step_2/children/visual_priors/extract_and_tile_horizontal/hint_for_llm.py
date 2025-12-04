HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: EXTRACT SHAPE AND TILE HORIZONTALLY           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
1. Find the bounding box of all non-zero cells in the input
2. Extract that rectangular region (the shape pattern)
3. Create output by placing TWO copies of this pattern side by side

OUTPUT DIMENSIONS:
• Height = bounding box height of the shape
• Width = 2 × bounding box width of the shape

STRUCTURE:
Input shape:     Output:
[pattern]   →    [pattern][pattern]

YOUR APPROACH:
• Identify all non-zero cells and find their min/max row and column
• Extract the rectangular subgrid defined by this bounding box
• Horizontally concatenate this subgrid with itself (tile 1×2)
"""
