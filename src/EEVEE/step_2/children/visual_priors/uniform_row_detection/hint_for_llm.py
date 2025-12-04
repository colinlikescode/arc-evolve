HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A UNIFORM ROW DETECTION PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Examine each row of the input independently
• A row is "UNIFORM" if ALL cells in that row contain the SAME value
• A row is "MIXED" if cells contain DIFFERENT values

OUTPUT CONSTRUCTION:
• For each UNIFORM row → fill the entire output row with a marker color
• For each MIXED row → fill the entire output row with the background color (zero/black)

KEY INSIGHT:
• The specific colors in the input don't matter - only whether each row is homogeneous
• The output uses exactly two colors: one for "uniform" rows, one for "mixed" rows
• This is essentially a row-by-row uniformity test

YOUR APPROACH:
1. For each row, check if all elements are equal
2. If uniform: output row = all marker color
3. If mixed: output row = all background color
"""
