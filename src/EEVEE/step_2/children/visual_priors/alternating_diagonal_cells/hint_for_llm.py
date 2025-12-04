HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ALTERNATING DIAGONAL CELLS PATTERN            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Non-zero cells form diagonal line segments in the input
• Along each diagonal segment, cells ALTERNATE between two colors
• The ORIGINAL color stays at certain positions (typically odd-indexed positions from start)
• A SECONDARY color replaces cells at alternating positions (typically even-indexed from start)
• Endpoints of diagonal segments often retain the original color

HOW TO IDENTIFY DIAGONALS:
• Trace connected sequences where each step moves +1 row and +1 column
• Each such sequence is treated as a separate diagonal segment

THE ALTERNATION PATTERN:
• Starting from one end of each diagonal segment
• Keep position 0 (original), change position 1, keep position 2, change position 3...
• OR the inverse pattern depending on segment boundaries

YOUR APPROACH:
1. Find all diagonal segments (connected non-zero cells moving diagonally)
2. For each segment, apply alternating color replacement
3. Preserve the original color at alternating positions, use secondary color at others
"""
