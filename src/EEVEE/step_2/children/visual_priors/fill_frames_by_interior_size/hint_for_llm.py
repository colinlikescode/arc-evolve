HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL FRAMES BY INTERIOR SIZE                  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains multiple rectangular frames (hollow boxes with a border color)
• Each frame has an interior region of varying size
• One small frame contains a single marked cell - this is the "key" showing which fill color maps to which size

HOW TO DETERMINE FILL COLORS:
• Find the smallest frame that has a single interior cell already colored - this tells you the fill color for 1-cell interiors
• Count the interior cells of each frame (width-2) × (height-2)
• Assign fill colors based on interior area:
  - Smallest interior area → one fill color
  - Medium interior area → another fill color  
  - Largest interior area → third fill color

YOUR APPROACH:
1. Identify all rectangular frames (border color surrounding background)
2. Calculate each frame's interior dimensions
3. Find the "key" frame (the one with a pre-filled single cell) to establish the color mapping
4. Fill each frame's interior with the appropriate color based on its size ranking
"""
