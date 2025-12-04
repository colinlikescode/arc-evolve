HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PARTITIONED REGION FILLING BY DIVIDER LINES  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A single non-background color forms DIVIDER LINES that partition the grid
• These lines create rectangular REGIONS of different sizes
• Identify all rectangular regions bounded by divider lines

FILLING LOGIC:
• The LARGEST rectangular region bounded by divider lines → fill with PRIMARY fill color
• SMALLER enclosed rectangular pockets (bounded on 3+ sides by dividers) → fill with SECONDARY marker color
• Regions open to the grid edge (not fully enclosed) → remain as background
• The divider lines themselves are PRESERVED unchanged

KEY INSIGHT:
• Find where divider lines form corners/junctions creating enclosed spaces
• The biggest enclosed area gets one color, small trapped pockets get another
• Look at the relationship between horizontal and vertical divider segments
"""
