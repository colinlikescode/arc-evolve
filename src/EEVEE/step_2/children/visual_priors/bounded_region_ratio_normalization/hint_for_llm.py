HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RATIO NORMALIZATION TO FIXED OUTPUT SIZE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a U-shaped or L-shaped frame (one distinct color) enclosing a region
• Within this frame: some rows are empty (background), some are filled (secondary color)
• The output is a fixed small grid (e.g., 3x3)

HOW TO COMPUTE:
1. Find the frame boundaries (vertical bars and bottom bar)
2. Count the TOTAL height of the interior region (rows between the vertical bars)
3. Count how many rows are FILLED vs EMPTY within that region
4. The output represents this ratio normalized to the output grid size:
   - Filled rows → secondary color in output (starting from top-left)
   - Empty rows → background color
5. The width ratio is similarly normalized

THINK OF IT AS:
• Measuring "how full" the container is
• Scaling that fullness to a standardized small grid
• Top-left corner of output = most filled, spreading based on ratio
"""
