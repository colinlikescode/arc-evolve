HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DOMINANT COLOR PRESERVATION PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Count the frequency of each color in the input grid
• Identify the DOMINANT color (the one appearing most often)
• Keep all cells with the dominant color UNCHANGED
• Replace ALL other cells (minority colors) with a single REPLACEMENT color

KEY OBSERVATIONS:
• The replacement color is consistent across all examples
• The dominant color is determined by simple frequency count
• Grid dimensions remain the same
• Only the minority colors change; dominant color is preserved exactly

YOUR APPROACH:
1. Count occurrences of each color in the input
2. Find which color has the highest count (dominant)
3. For each cell: if it matches dominant → keep it; otherwise → use replacement color
"""
