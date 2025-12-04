HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: STRIPE EXTRACTION WITH MASK REGION            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains parallel stripes (horizontal or vertical) of different colors
• A rectangular "mask" region (filled with a single repeated color) occludes part of the grid
• The mask region defines the OUTPUT DIMENSIONS

YOUR TASK:
1. Identify all distinct stripe colors (excluding background and mask color)
2. Determine the stripe orientation (horizontal or vertical)
3. Order stripes by their position in the input (top→bottom or left→right)
4. The output width/height comes from the mask region's perpendicular dimension
5. Create output: one row/column per stripe, filled with that stripe's color

KEY INSIGHT:
• The mask region's size tells you how wide/tall each output row/column should be
• Count the number of distinct colored stripes to get the other output dimension
• Preserve the spatial ordering of stripes from input to output
"""
