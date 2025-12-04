HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HIGHLIGHT COMPLETE 2x2 BLOCKS                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has a background color and a secondary (non-background) color
• Find all locations where the secondary color forms a COMPLETE 2x2 block
• Replace those 2x2 blocks with a new marker/highlight color
• All other cells remain unchanged

WHAT TO LOOK FOR:
• Scan for every position (r, c) where cells at (r,c), (r,c+1), (r+1,c), (r+1,c+1) ALL contain the secondary color
• These complete 2x2 squares get "painted over" with the highlight color
• The highlight color is distinct from both the background and secondary colors

KEY INSIGHT:
• Only PERFECT 2x2 blocks of the secondary color get highlighted
• Partial or incomplete groupings remain unchanged
"""
