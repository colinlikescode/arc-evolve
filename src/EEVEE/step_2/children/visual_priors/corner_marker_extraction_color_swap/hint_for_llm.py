HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CORNER-MARKER EXTRACTION WITH COLOR SWAP     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find 4 cells of the SAME color that form corners of a rectangle (marker color)
• These markers define a bounding region in the input
• Inside this region, there is a pattern made of a DIFFERENT color (pattern color)
• Extract ONLY the region bounded by (but not including) the corner markers
• In the output: replace the pattern color with the marker color
• Background cells remain as background

KEY OBSERVATIONS:
• Corner markers are always the same color and form axis-aligned rectangle corners
• The pattern inside uses a different non-background color
• Output dimensions = (marker_bottom_row - marker_top_row - 1) × (marker_right_col - marker_left_col - 1)
• Color swap: pattern_color → marker_color

YOUR CODE MUST:
1. Identify the corner marker color (appears exactly 4 times in rectangular arrangement)
2. Find the bounding rectangle defined by these markers
3. Extract the interior region (excluding marker rows/columns)
4. Replace all pattern-colored cells with the marker color
"""
