HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RANK VERTICAL LINES BY LENGTH                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all vertical lines of the marker color (non-zero, non-background)
• Each line starts at a different row and extends to the bottom
• Calculate the LENGTH of each line (from first appearance to bottom)
• RANK the lines by length: longest = rank 1, second longest = rank 2, etc.
• Replace each marker color with its RANK NUMBER as the new color

KEY OBSERVATIONS:
• The longest vertical line becomes color 1
• The second longest becomes color 2
• Continue with 3, 4, etc. for shorter lines
• Lines of equal length should be handled consistently
• The grid structure (positions) stays the same, only colors change

YOUR APPROACH:
1. Identify column positions containing the marker color
2. For each column, find the first row where the marker appears
3. Calculate length = (total_rows - first_row)
4. Sort columns by length (descending) to determine rank
5. Replace marker cells in each column with their rank number
"""
