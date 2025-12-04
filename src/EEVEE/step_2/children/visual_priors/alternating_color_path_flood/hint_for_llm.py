HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PATH FLOODING WITH ALTERNATING COLORS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the small SEED PATTERN: a cross/plus shape made of TWO alternating colors
• The seed has a CENTER color and an EDGE color (pattern: edge-center-edge)
• These two colors FLOOD outward along all connected PATH cells
• PATH cells are the non-wall, non-seed color (typically zeros)

PROPAGATION BEHAVIOR:
• Starting from the seed, colors alternate as they extend along paths
• Each step along a path switches between the two seed colors
• The pattern maintains parity: cells at even distance get one color, odd distance get the other
• Wall cells and the original structure remain unchanged

YOUR APPROACH:
1. Identify the wall color (most frequent) and path color
2. Find the seed cross pattern and extract its two alternating colors
3. From the seed, flood-fill along path cells with alternating colors
4. Preserve all wall cells in their original positions
"""
