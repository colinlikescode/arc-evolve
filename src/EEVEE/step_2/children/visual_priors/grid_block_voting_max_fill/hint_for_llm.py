HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID BLOCK VOTING / MAX MARKER SELECTION      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into blocks by separator lines (a consistent divider color)
• Each block contains some scattered marker cells of a "vote" color
• Count the number of markers in each block
• The block with the MAXIMUM count wins
• Fill the winning block ENTIRELY with the marker color
• Clear ALL other blocks to the background color (keep separators intact)

HOW TO SOLVE:
1. Identify the separator color (forms complete rows/columns)
2. Identify the marker color (scattered non-zero, non-separator cells)
3. Divide the grid into blocks based on separator lines
4. Count markers in each block
5. Find the block with the highest count
6. Output: Fill that block solid with the marker color, clear all others

KEY INSIGHT: This is a "voting" puzzle - each marker is a vote, and the block with the most votes wins and gets filled completely.
"""
