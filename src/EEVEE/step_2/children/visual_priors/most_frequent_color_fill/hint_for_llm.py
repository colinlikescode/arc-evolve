HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A MOST FREQUENT COLOR FILL PUZZLE     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count the frequency of each color in the input grid
• Identify which color appears MOST OFTEN
• Fill the ENTIRE output grid with that most frequent color

KEY OBSERVATIONS:
• The output grid has the same dimensions as the input
• The output is completely uniform (all cells are the same color)
• The chosen color is determined by frequency counting, NOT by position

YOUR APPROACH MUST:
1. Flatten or iterate through all cells in the input
2. Count occurrences of each distinct color value
3. Find the color with the maximum count
4. Create an output grid of the same size, filled entirely with that color
"""
