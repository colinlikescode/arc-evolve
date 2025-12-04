HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: QUADRANT COLOR MAPPING WITH CORNER MARKERS    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid has separator lines (uniform color) dividing it into quadrants
• Four corners contain unique marker colors - these are the "color keys"
• The interior region has a pattern made with an indicator color
• The output extracts the interior pattern and recolors it

COLOR MAPPING BY QUADRANT:
• Divide the interior pattern into 4 quadrants (top-left, top-right, bottom-left, bottom-right)
• Each quadrant inherits the color from its corresponding corner marker
• Where the indicator color appears in a quadrant → replace with that quadrant's corner color
• Background cells remain as background

YOUR APPROACH:
1. Identify the separator color (forms horizontal and vertical lines)
2. Extract the four corner marker colors
3. Extract the interior pattern region (between separator lines)
4. For each cell in the interior pattern:
   - Determine which quadrant it belongs to
   - If it has the indicator color, replace with the corresponding corner's marker color
   - Otherwise, keep as background
"""
