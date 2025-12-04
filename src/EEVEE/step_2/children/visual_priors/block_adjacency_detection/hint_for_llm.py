HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: BLOCK ADJACENCY DETECTION PUZZLE              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains 2x2 blocks of TWO different non-background colors
• One color type acts as "markers" and the other as "targets"
• Count how many marker blocks exist (this determines output width)
• For EACH marker block, check if a target block is directly adjacent to it

OUTPUT CONSTRUCTION:
• Output is a single row with one cell per marker block
• If a marker block touches a target block → output one value
• If a marker block is isolated (no adjacent target) → output another value
• Process marker blocks in a consistent order (e.g., top-to-bottom, left-to-right)

KEY INSIGHT:
• Isolated single cells of either color are NOISE - ignore them
• Only consider complete 2x2 blocks
• "Adjacent" means the blocks share an edge (horizontally or vertically touching)
"""
