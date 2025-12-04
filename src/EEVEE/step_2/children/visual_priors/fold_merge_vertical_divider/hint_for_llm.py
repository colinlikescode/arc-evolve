HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A FOLD-AND-MERGE PUZZLE               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a vertical DIVIDER COLUMN running top to bottom
• This divider splits the grid into LEFT and RIGHT halves
• The transformation FOLDS one half onto the other and MERGES them

HOW TO SOLVE:
1. Identify the vertical separator column (consistent single color top-to-bottom)
2. Extract the LEFT portion (columns before the separator)
3. Extract the RIGHT portion (columns after the separator)
4. FLIP the left portion horizontally
5. OVERLAY/MERGE the flipped left with the right:
   - For each cell, take the non-background value if one exists
   - If both have non-background values, either may appear

OUTPUT DIMENSIONS:
• Height = input height
• Width = number of columns on one side of the divider

Think of it like folding a piece of paper along the divider line and seeing the combined pattern.
"""
