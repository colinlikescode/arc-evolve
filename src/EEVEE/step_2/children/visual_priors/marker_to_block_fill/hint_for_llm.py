HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-TO-BLOCK REGION FILLING PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into equal-sized rectangular regions (blocks)
• Each marker cell in the input acts as a "flag" for its containing region
• If a region contains ANY marker cell → fill the ENTIRE region with the fill color
• If a region has NO markers → keep it as background (zeros)

HOW TO SOLVE:
1. Determine the block/region size by dividing grid dimensions by number of regions
2. For each region in the grid:
   - Check if ANY cell in that region contains a marker (non-zero value)
   - If yes: fill the entire region with the output fill color
   - If no: leave the region as background
3. The marker positions within a region don't matter - only their presence

KEY INSIGHT: Markers are sparse indicators; their exact position within a block 
is irrelevant - only whether a block CONTAINS a marker determines if it gets filled.
"""
