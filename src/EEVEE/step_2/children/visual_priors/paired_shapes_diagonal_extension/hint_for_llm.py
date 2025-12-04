HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PAIRED SHAPES WITH DIAGONAL CONNECTIONS       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple small shapes of the same non-zero color
• Each shape has an "open" direction or "pointing" end (like an L-shape or corner)
• From the tip/corner of each shape, draw a diagonal line extending outward
• The diagonal continues in the direction the shape "points" until reaching the grid boundary

HOW TO IDENTIFY THE DIAGONAL DIRECTION:
• Find the "apex" or single-cell tip of each shape
• The diagonal extends AWAY from the bulk of the shape
• If a shape has cells forming an L, the diagonal goes from the corner outward

CONCEPTUAL APPROACH:
1. Identify all connected components of non-zero cells
2. For each shape, find its "pointing" direction (the corner/apex)
3. From that apex, draw a diagonal line (moving one step in both row and column each time)
4. Continue until the grid boundary is reached
5. Keep all original cells unchanged

The shapes remain in place; only diagonal extensions are added.
"""
