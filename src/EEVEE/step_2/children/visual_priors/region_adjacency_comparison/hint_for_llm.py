HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: REGION ADJACENCY COMPARISON PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all distinct solid rectangular blocks of one color (the "region" color)
• Identify scattered single cells of another color (the "marker" color)
• For each rectangular region, count how many marker cells are orthogonally adjacent to it (touching its border)
• Compare the adjacency counts between the regions

OUTPUT DETERMINATION:
• If the regions have EQUAL adjacency counts → output the background color (0)
• If the regions have UNEQUAL adjacency counts → output the marker color

YOUR APPROACH:
1. Find all solid 2x2 (or similar) blocks of the same non-background, non-marker color
2. For each block, count adjacent marker-colored cells (including diagonals or orthogonal only)
3. Compare counts and output accordingly
"""
