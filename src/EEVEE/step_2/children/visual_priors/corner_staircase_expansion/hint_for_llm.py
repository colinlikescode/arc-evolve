HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CORNER MARKER STAIRCASE EXPANSION             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each corner marker spawns a triangular staircase pattern
• The staircase grows FROM the corner TOWARD the grid center
• Pattern alternates: filled row, empty row, filled row...
• Each filled row extends ONE cell further than the previous filled row
• The pattern uses the corner marker's color

STAIRCASE STRUCTURE (from a corner):
Row 0: color at corner, skip, color, skip, color... (every other cell)
Row 1: empty (or partial)
Row 2: solid block of 3 cells
Row 3: empty
Row 4: solid block of 5 cells
...and so on, growing toward center

CORNER BEHAVIOR:
• Top-left corner: grows DOWN and RIGHT
• Top-right corner: grows DOWN and LEFT  
• Bottom-left corner: grows UP and RIGHT
• Bottom-right corner: grows UP and LEFT

Each region expands until it meets the center or another region.
"""
