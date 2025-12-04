HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: QUADRANT COLOR MAPPING WITH 2x2 KEY           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a separator line dividing it into regions
• Find the 2x2 color key block (contains 4 different non-zero, non-separator colors)
• Find the pattern region (marked with a single template/marker color)
• The pattern region is conceptually divided into 4 quadrants (2 rows × 2 cols of sub-blocks)

COLOR MAPPING:
• The 2x2 key maps position-to-quadrant:
  - Key[0,0] → replaces markers in top-left quadrant
  - Key[0,1] → replaces markers in top-right quadrant
  - Key[1,0] → replaces markers in bottom-left quadrant
  - Key[1,1] → replaces markers in bottom-right quadrant

OUTPUT CONSTRUCTION:
• Extract the pattern region (excluding separator)
• Replace the marker color in each quadrant with the corresponding key color
• Background (zero) cells remain as background
"""
