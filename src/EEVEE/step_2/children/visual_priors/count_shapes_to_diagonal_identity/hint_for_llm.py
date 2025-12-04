HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COUNT SHAPES → DIAGONAL IDENTITY PATTERN      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count the number of DISTINCT connected regions (shapes) of non-zero cells in the input
• Let N = the count of distinct shapes
• Create an N×N output grid filled with background color
• Place the non-zero color ONLY on the main diagonal (positions [0,0], [1,1], [2,2], ... [N-1,N-1])

KEY INSIGHT:
• Each separate "blob" or connected component of colored cells counts as ONE shape
• Shapes are separated by background cells (not touching, even diagonally in most cases)
• The output is always a square "identity matrix" pattern

YOUR APPROACH:
1. Identify all connected components of non-zero cells in the input
2. Count how many distinct components exist → this gives N
3. Create N×N grid with non-zero color on the diagonal only
"""
