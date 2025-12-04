HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL LINE DRAWING BETWEEN MATCHING PAIRS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each distinct non-zero color appears EXACTLY TWICE in the input
• For each pair of same-colored cells, draw a diagonal line connecting them
• The diagonal moves one row and one column per step toward the target
• Fill all cells along this diagonal path with that color

HOW TO FIND THE DIAGONAL:
• Identify the two positions (r1, c1) and (r2, c2) for each color
• Determine direction: row_step = sign(r2-r1), col_step = sign(c2-c1)
• Starting from (r1, c1), repeatedly add (row_step, col_step) until reaching (r2, c2)
• Mark each cell along this path with the color

IMPORTANT:
• Original cells remain in place
• Only the diagonal path between pairs gets filled
• Each color pair is processed independently
• Lines are always diagonal (not horizontal or vertical)
"""
