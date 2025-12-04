HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECT THE MOST COMPLETE SHAPE PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple distinct colored regions (different non-zero colors)
• Each region has a bounding box containing its cells
• Calculate the "completeness" of each region: count of filled cells / total cells in bounding box
• The output is the MOST COMPLETE region extracted to its bounding box size

HOW TO IDENTIFY THE WINNER:
• Find all distinct non-zero colors in the input
• For each color, find its bounding box
• Count how many cells within that bounding box are filled vs empty (zeros)
• The shape with the HIGHEST fill ratio (most rectangular/solid) is the answer

OUTPUT FORMAT:
• Extract the winning shape's bounding box exactly as it appears
• The output grid dimensions match the bounding box of the selected shape
• Preserve the original color and any internal zeros/gaps
"""
