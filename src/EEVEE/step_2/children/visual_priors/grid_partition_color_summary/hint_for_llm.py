HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID PARTITION TO COLOR MAP PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into rectangular regions by separator lines (rows/columns of background color)
• Each region contains predominantly ONE non-zero color with some background cells mixed in
• The output is a condensed grid where each cell = the dominant non-zero color of the corresponding region

HOW TO SOLVE:
1. Find separator lines (full rows/columns of zeros) that partition the grid
2. Identify the rectangular regions created by these separators
3. For each region, determine the dominant non-zero color (the color that fills most cells)
4. Create output grid with dimensions = (number of region rows) × (number of region columns)
5. Place each region's dominant color in the corresponding output cell

SPATIAL MAPPING:
• Top-left input region → top-left output cell
• Regions map to output cells preserving their relative positions
• The output is essentially a "thumbnail" showing the color of each region
"""
