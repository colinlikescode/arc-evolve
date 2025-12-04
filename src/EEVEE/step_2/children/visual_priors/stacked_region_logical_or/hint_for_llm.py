HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LOGICAL OR OF TWO STACKED REGIONS             ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• The grid has a horizontal DIVIDER ROW (uniform color across entire row)
• Above the divider: REGION A (a binary-like pattern)
• Below the divider: REGION B (another binary-like pattern)
• Both regions have the same dimensions

THE TRANSFORMATION RULE:
• Output size = size of one region (same as Region A or Region B)
• For each cell position (row, col):
  - If Region A OR Region B has a non-background value → output a MARKER COLOR
  - If BOTH regions have background/zero → output remains background/zero

CONCEPTUALLY:
• This is a LOGICAL OR operation between two pattern masks
• The two input regions use different non-background colors
• The output uses a NEW color to show the union of both patterns
• The divider row is discarded in the output
"""
