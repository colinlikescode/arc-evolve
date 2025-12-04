HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL DIVIDER COMPARISON PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a vertical separator column (distinct color) dividing it into LEFT and RIGHT halves
• The output grid has the same dimensions as each half
• Compare corresponding cells from the left half and right half
• Mark cells in the output where BOTH halves have the SAME non-background value at that position
• Use a special marker color for matches, background color (zero) for non-matches

CONCEPTUAL LOGIC:
• Find the separator column (unique color forming a vertical line)
• Extract the left region (before separator) and right region (after separator)
• For each position (row, col):
  - If left[row][col] AND right[row][col] are BOTH non-zero AND EQUAL → mark with output color
  - Otherwise → leave as background (zero)

The output essentially shows the INTERSECTION of non-zero patterns from both halves.
"""
