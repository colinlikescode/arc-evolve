HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SPLIT-GRID XOR COMPARISON PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a SEPARATOR ROW (uniform distinct color) dividing it horizontally
• This creates TWO REGIONS of equal size above and below the separator
• Both regions use a primary color and background (zero)

THE OUTPUT IS AN XOR COMPARISON:
• Output dimensions = dimensions of one region (excluding separator)
• For each cell position (r, c):
  - If TOP[r][c] has primary AND BOTTOM[r][c] has primary → background
  - If TOP[r][c] has background AND BOTTOM[r][c] has background → background  
  - If EXACTLY ONE has primary (they DIFFER) → mark with result color

CONCEPTUALLY:
• Find the separator row (all cells same non-background, non-primary color)
• Extract the region above and the region below
• XOR the two regions: differences become marked, matches become background
• The result color is a NEW color not present in the original regions
"""
