HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SIZE-BASED COLOR RANKING PUZZLE     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all distinct non-zero colored regions in the input
• Count the number of cells in each colored region
• Rank the colors by their region size (largest to smallest)
• Output a single column with colors listed in size order

KEY OBSERVATIONS:
• Each distinct non-zero color forms one connected or scattered region
• The output has exactly as many rows as there are distinct colors
• The first row contains the color with the MOST cells
• The last row contains the color with the FEWEST cells

YOUR APPROACH:
1. Find all unique non-zero colors in the input
2. For each color, count how many cells contain that color
3. Sort colors by cell count in DESCENDING order
4. Create output as a single column with colors in sorted order
"""
