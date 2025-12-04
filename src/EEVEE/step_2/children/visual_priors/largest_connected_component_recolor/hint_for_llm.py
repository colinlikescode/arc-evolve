HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: LARGEST CONNECTED COMPONENT RECOLORING        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all connected components of non-zero cells (using 4-connectivity)
• Find the LARGEST connected component by cell count
• Recolor all cells in that largest component to a NEW non-zero color
• Leave all other non-zero cells unchanged (smaller components, isolated cells)

KEY CONCEPTS:
• Connected = adjacent horizontally or vertically (not diagonal)
• A connected component is a maximal set of non-zero cells where you can reach any cell from any other by moving through adjacent non-zero cells
• Only the largest group changes; everything else stays the same

YOUR APPROACH:
1. Find all connected components of non-zero cells
2. Determine which component has the most cells
3. Replace the color of cells in that largest component with the new marker color
4. Keep all other cells (background and smaller components) unchanged
"""
