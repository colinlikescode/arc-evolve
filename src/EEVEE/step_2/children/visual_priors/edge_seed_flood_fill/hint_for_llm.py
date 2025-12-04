HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LEFT-EDGE CELL FLOOD FILL                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. FIND THE SOURCE CELL:
   - Look for a single colored cell on the LEFT EDGE (column 0)
   - This cell is isolated (no colored neighbors)
   - This is the FLOOD FILL SOURCE

2. FLOOD FILL from the left-edge cell:
   - Start from the source cell position
   - Fill all reachable black (0) cells with the source color
   - Spread in all 4 cardinal directions (up, down, left, right)

3. STOP at colored obstacles:
   - Any non-zero colored cell BLOCKS the flood
   - These cells remain unchanged - they act as WALLS
   - The flood cannot pass through them

ALGORITHM:
```python
1. Find the isolated cell on the left edge (column 0)
2. flood_color = that cell's color
3. BFS/DFS flood fill:
   - Start from source position
   - For each cell, try to spread to neighbors
   - If neighbor is 0 (black), fill it and continue
   - If neighbor is non-zero, STOP (it's a wall)
4. Return the filled grid
```

RESULT: Large regions filled with the source color, original colored cells preserved as obstacles.

KEY: The single cell on the LEFT EDGE is the flood fill source!
"""

