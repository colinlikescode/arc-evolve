HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SPLIT-GRID LOGICAL OR/UNION PATTERN          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is split into TWO equal halves (left and right)
• Each half contains its own distinct marker color on a background
• The output has the same dimensions as ONE half

LOGICAL OPERATION:
• For each position (row, col) in the output:
  - Check if the LEFT half has a non-background cell at that position
  - Check if the RIGHT half has a non-background cell at that position
  - If EITHER is non-background → output a unified marker color
  - If BOTH are background → output background

This is essentially: output = left_pattern OR right_pattern

The output uses a NEW color (not present in input) to mark all combined positions.
"""
