HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A LOGICAL XOR COMPARISON PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• The input contains TWO grids stacked vertically, separated by a uniform horizontal divider row
• Each grid section uses a binary pattern: background (zero) vs non-background cells

THE TRANSFORMATION RULE:
• Compare the two grid sections cell-by-cell
• Output marks cells where EXACTLY ONE section has a non-background value
• This is the XOR (exclusive OR) operation:
  - If top has value AND bottom has value → output background
  - If top has value AND bottom is empty → output marked
  - If top is empty AND bottom has value → output marked
  - If both are empty → output background

KEY INSIGHT:
• Ignore the separator row entirely (it just divides the two comparison regions)
• The output uses a NEW color (different from both input colors) to mark XOR results
• Output size equals the size of each individual section (not the full input)
"""
