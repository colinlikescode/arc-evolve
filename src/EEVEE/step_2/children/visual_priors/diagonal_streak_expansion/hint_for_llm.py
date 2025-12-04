HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL STREAK/TRAIL EXPANSION PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input: A single row of width W with some non-zero elements
• Find the FIRST non-zero element's position (0-indexed from left) = F
• Output size: (W × (W - F)) rows × (W × (W - F)) columns (square grid)

HOW THE DIAGONAL WORKS:
• The input row pattern "slides" diagonally from top-right to bottom-left
• Each row of output places the input pattern shifted one position left from the previous row
• The first non-zero element starts at the rightmost column in row 0
• The pattern continues until the first non-zero element reaches the leftmost column
• Zeros in the input remain zeros; non-zero values preserve their relative positions

VISUAL PATTERN:
• Row 0: pattern starts at far right, first non-zero at last column
• Row 1: pattern shifts left by 1
• Row 2: pattern shifts left by 2
• ... continues until pattern reaches left edge

The key insight: Output height = Output width = (input_width - first_nonzero_index) × some factor based on the rightmost non-zero position.
"""
