HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: STRAY MARKERS ATTRACT TO DIVIDING LINES       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains one or more DIVIDING LINES (full rows or columns of a single color)
• STRAY MARKERS are isolated cells that share a color with a dividing line
• Each stray marker MOVES to become adjacent to its matching dividing line

HOW TO PROCESS:
1. Identify all dividing lines (complete rows or columns of one color)
2. Find all stray markers (isolated cells matching a dividing line's color)
3. For each stray marker:
   - Remove it from its current position
   - Place a cell of the same color ADJACENT to the matching dividing line
   - Preserve the marker's row (if line is vertical) or column (if line is horizontal)
   - Place it on the side of the line that is CLOSER to the marker's original position

IMPORTANT: The dividing lines themselves remain unchanged. Only the stray markers relocate.
"""
