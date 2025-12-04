HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID CELL COLORING BY DEFECT DETECTION        ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• A grid divided by separator lines (single non-background color) into rectangular cells
• Some separator positions have "defects" (gaps where separator is missing)

THE TRANSFORMATION RULE:
• Identify the grid structure: find the separator color and cell boundaries
• For each cell, check if ANY of its bordering separator positions have defects
• Cells with NO defects on their borders → fill with COLOR_A
• Cells with ANY defects on their borders → fill with COLOR_B
• Preserve all separator line positions
• Defect positions (gaps in separators) get filled with COLOR_B

KEY INSIGHT:
• A defect "contaminates" the cells adjacent to it
• Clean cells (no adjacent defects) get one color
• Contaminated cells (at least one adjacent defect) get another color
• The defects themselves also get the contaminated color
"""
