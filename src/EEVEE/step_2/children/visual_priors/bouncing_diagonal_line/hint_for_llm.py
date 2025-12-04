HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BOUNCING DIAGONAL LINE PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the single non-zero cell in the input (always at bottom-left corner)
• Create a diagonal line that "bounces" between the left and right edges
• The line moves upward one row at a time, changing column position diagonally
• When hitting the left edge (column 0), the line bounces right
• When hitting the right edge (last column), the line bounces left
• Each row has exactly ONE non-zero cell marking the path

CONCEPTUAL BEHAVIOR:
• Think of a ball bouncing between two walls as it rises
• Starting position determines the initial direction
• The period of the zigzag pattern is 2×(width-1)
• Track column position and direction (+1 or -1) as you move up each row

OUTPUT STRUCTURE:
• Same dimensions as input
• One non-zero cell per row forming the bouncing path
• The non-zero color from input is used for the entire path
"""
