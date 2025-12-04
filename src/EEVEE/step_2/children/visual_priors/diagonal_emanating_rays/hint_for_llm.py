HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL EMANATING RAYS FROM SEED POINT       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-background cell (the "seed") - it stays in place
• Draw two diagonal rays extending from the seed in OPPOSITE diagonal directions
• One ray goes toward upper-right, the other toward lower-left (or vice versa)

EACH RAY STRUCTURE:
• Rays are made of repeating L-shaped corner segments
• Each L-segment consists of: one cell directly adjacent to seed (vertically), 
  then a horizontal bar of 3 cells extending diagonally outward
• Segments repeat, stepping 2 cells diagonally each iteration
• Use a secondary/marker color (different from both background and seed)

PATTERN PROGRESSION:
• First segment: 1 step from seed
• Each subsequent segment: 2 more steps diagonally outward
• Continue until reaching grid boundaries

YOUR CODE MUST:
1. Locate the single non-background cell (seed position)
2. For each of the two opposite diagonal directions:
   - Draw L-shaped segments stepping outward
   - Each segment: vertical cell + horizontal 3-cell bar
   - Repeat until boundary reached
"""
