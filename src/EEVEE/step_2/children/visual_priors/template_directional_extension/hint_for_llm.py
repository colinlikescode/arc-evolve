HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  TEMPLATE-BASED DIRECTIONAL EXTENSION PUZZLE             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TEMPLATE: a small pattern with two colors - a "shape" color and a "marker" color
• The marker color in the template indicates the DIRECTION of extension (the shape extends AWAY from the markers)
• Find all ANCHOR BLOCKS: rectangles of only the marker color elsewhere in the grid
• For each anchor block, EXTEND the shape pattern outward from the anchor
• The extension is SCALED by the anchor block's dimensions (if anchor is 2×2, each cell of the template becomes 2×2)

DIRECTION LOGIC:
• If markers are to the RIGHT of the shape → extend LEFT from anchor
• If markers are BELOW the shape → extend UP from anchor
• If markers are on multiple sides → extend in all opposite directions

YOUR APPROACH:
1. Identify the template pattern and extract the shape + marker positions
2. Determine which direction(s) the shape extends relative to markers
3. For each anchor block, apply the scaled shape in the opposite direction(s)
4. Keep the original template and anchor blocks in place
"""
