HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DIVIDED REGION XOR COMPARISON       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is split by a vertical divider column into LEFT and RIGHT regions
• Each region has its own pattern color on a background
• The output has the same dimensions as each region (excluding the divider)

COMPARISON LOGIC (XOR):
• For each cell position in the two regions:
  - If LEFT has pattern AND RIGHT has pattern → output background
  - If LEFT has pattern AND RIGHT is empty → output marker color
  - If LEFT is empty AND RIGHT has pattern → output marker color
  - If BOTH are empty → output background

IN OTHER WORDS:
• Output marks positions where EXACTLY ONE region has a non-background cell
• This is a logical XOR between the two pattern regions
• Use a new marker color (not from input) for the output pattern

YOUR CODE MUST:
1. Find the divider column (single distinct value forming a vertical line)
2. Extract the left and right regions
3. Compare cell-by-cell: mark output where patterns differ (XOR)
"""
