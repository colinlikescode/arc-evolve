HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: UNIQUE SUB-GRID SELECTION PUZZLE              ║
╚══════════════════════════════════════════════════════════════╝

THE GRID STRUCTURE:
• The input is divided into sub-grids by separator lines (full rows/columns of one color)
• This creates a matrix of sub-regions (typically 3×3)

THE TRANSFORMATION RULE:
• Keep the separator lines intact in the output
• Clear ALL sub-grids to background EXCEPT one
• The ONE sub-grid to preserve is the "unique" one

HOW TO FIND THE UNIQUE SUB-GRID:
• Compare corresponding positions across all sub-grids
• For each position, count how many sub-grids have non-zero values there
• The unique sub-grid is the one where its non-zero cells appear at positions where ALL other sub-grids have zeros (it has exclusive content)
• Alternatively: find the sub-grid whose pattern doesn't overlap/conflict with the union of all others

YOUR APPROACH:
1. Identify separator lines and extract sub-grids
2. For each sub-grid, check if its non-zero positions are unique (zeros in all other sub-grids at those positions)
3. Output = separators + the unique sub-grid's content (all other sub-grids cleared)
"""
