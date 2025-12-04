HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TILED DOUBLING WITH DIAGONAL MARKER OVERLAY   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:

1. SIZE TRANSFORMATION:
   • Output dimensions = 2 × input dimensions (both width and height)
   • The input is conceptually tiled 2×2 to create the base output

2. PRESERVE SPECIAL CELLS:
   • Non-background colored cells from the input appear at their corresponding tiled positions
   • These cells are repeated in each of the 4 quadrants

3. DIAGONAL MARKER OVERLAY:
   • A marker color (not present in input) fills certain background cells
   • For each special colored cell position, draw diagonal lines emanating from it
   • The marker appears where diagonals from different special cells would intersect or extend
   • Think of it as: each special cell "projects" diagonal rays, and where those rays hit background cells, place the marker

4. PRIORITY:
   • Original special colored cells take precedence over the marker color
   • Background cells that lie on diagonal paths from special cells become marker-colored

YOUR APPROACH:
- First tile the input 2×2
- Identify positions of non-background cells
- For each such position, trace diagonals and mark intersecting background cells
- Preserve original colored cells over marker overlay
"""
