HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRID PARTITION WITH DIAGONAL MARKING          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A divider color creates horizontal and vertical lines that partition the grid into cell regions
• Think of it as a table/grid structure where divider lines are the borders
• The transformation fills THREE specific cell regions with three distinct marker colors:
  1. FIRST marker color → the TOP-LEFT corner cell region
  2. SECOND marker color → the CENTER diagonal cell region (middle of the grid)
  3. THIRD marker color → the BOTTOM-RIGHT corner cell region

HOW TO IDENTIFY REGIONS:
• Find all horizontal divider lines (full rows of the divider color)
• Find all vertical divider lines (full columns of the divider color)
• These lines define the boundaries of rectangular cell regions
• Count cell positions by their row-band and column-band indices

THE DIAGONAL CELLS TO MARK:
• Cell at grid position (0, 0) → first marker color
• Cell at the center of the diagonal → second marker color
• Cell at the last diagonal position (bottom-right) → third marker color

Keep divider lines unchanged; only fill the background regions.
"""
