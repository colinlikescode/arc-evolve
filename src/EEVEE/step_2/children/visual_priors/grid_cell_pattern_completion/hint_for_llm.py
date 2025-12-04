HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID-DIVIDED PATTERN COMPLETION PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE STRUCTURE:
• The grid is divided into equal rectangular cells by lines of a "divider" color
• One cell contains a COMPLETE reference shape (the "template")
• Other cells contain PARTIAL fragments or are EMPTY

THE TRANSFORMATION RULE:
• Find the complete reference shape in one cell - this is your template
• For each other cell in the grid:
  - If the cell has fragment(s) of a shape: overlay the template using the DIVIDER color, but PRESERVE the original fragment pixels
  - If the cell is empty: fill the template positions with the DIVIDER color
  - The cell with the complete shape stays unchanged

KEY INSIGHT:
• Fragments indicate "keep these pixels as the shape color"
• Missing parts of the shape get filled with the divider/grid color
• Empty cells get the full template shape drawn in the divider color

YOUR CODE MUST:
1. Identify the divider color (forms grid lines)
2. Identify cell boundaries
3. Find the complete reference shape
4. For each cell: merge template with existing fragments, using divider color for missing parts
"""
