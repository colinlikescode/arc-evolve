HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL STRIPE VALIDATION PATTERN            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has a repeating diagonal stripe pattern
• For each column c, there is an "expected" row: row = c mod (number of rows)
• This creates diagonal stripes going from top-left to bottom-right, wrapping

FOR EACH NON-ZERO MARKER IN THE INPUT:
• If the marker is at position (row, col) where row == col mod num_rows:
  → The marker is ON the diagonal → KEEP original color
• If the marker is at position (row, col) where row != col mod num_rows:
  → The marker is OFF the diagonal → CHANGE to alternate color

The alternate color is a different non-background, non-marker color.

VISUAL PATTERN:
For a 3-row grid, the diagonal ownership repeats:
Col:  0 1 2 3 4 5 6 7 8 ...
Row:  0 1 2 0 1 2 0 1 2 ...

Markers matching this pattern stay unchanged; others get recolored.
"""
