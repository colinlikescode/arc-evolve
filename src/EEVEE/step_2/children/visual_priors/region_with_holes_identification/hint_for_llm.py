HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND THE REGION WITH INTERNAL HOLES           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple colored rectangular regions on a background
• Most regions are SOLID (completely filled with their color)
• ONE region has HOLES (background cells inside its bounding rectangle)
• The output is a 1x1 grid containing the color of the imperfect/holey region

HOW TO IDENTIFY THE HOLEY REGION:
• For each distinct non-background color, find its bounding box
• Check if the bounding box is completely filled with that color
• The region that is NOT completely filled (has background cells inside) is the answer

YOUR OUTPUT:
• Return a 1x1 grid with the color of the region containing holes
"""
