HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECT THE LARGEST SHAPE BY CELL COUNT        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains MULTIPLE distinct colored shapes on a background
• Each shape has a different color
• Your task: IDENTIFY and EXTRACT the shape with the MOST cells

STEPS TO SOLVE:
1. Find all distinct non-background colors in the input
2. For each color, COUNT how many cells have that color
3. Select the color with the MAXIMUM cell count
4. Extract that shape's bounding box (crop to its extent)
5. Output the cropped region containing only that shape

KEY INSIGHT:
• The "largest" shape means the one with the most non-zero cells
• NOT the one with the largest bounding box
• The output preserves the shape exactly, cropped to fit
"""
