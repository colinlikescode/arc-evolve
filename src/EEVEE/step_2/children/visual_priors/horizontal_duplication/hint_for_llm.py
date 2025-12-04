HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A HORIZONTAL DUPLICATION PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The output is the input concatenated horizontally with itself
• Output dimensions: same height, double the width
• Left half of output = exact copy of input
• Right half of output = exact copy of input

VISUAL REPRESENTATION:
Input:          Output:
[PATTERN]  →    [PATTERN][PATTERN]

YOUR APPROACH:
1. Keep the same number of rows
2. For each row, duplicate the row's contents by appending it to itself
3. The result is the input "tiled" once horizontally

This is a simple horizontal concatenation - no rotation, reflection, or modification of values.
"""
