HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ADJACENT MARKER PAIR REPLACEMENT PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two specific colors act as "paired markers" - identify which two colors appear adjacent to each other
• A third color type acts as "anchors" and never changes
• When the two marker colors are horizontally or vertically adjacent:
  - One marker gets REPLACED with a new indicator color
  - The other marker gets REMOVED (becomes background/zero)
• Marker instances that are NOT adjacent to their pair partner remain unchanged

HOW TO IDENTIFY THE COLORS:
• The "anchor" color: appears in input and output unchanged
• The "marker pair" colors: two colors that appear adjacent; one transforms to a new color, one disappears
• The "replacement" color: appears in output but not in input

YOUR APPROACH:
1. Identify which color is the anchor (unchanged between input/output)
2. Identify the two marker colors that form adjacent pairs
3. For each adjacent pair found, replace one with the new color and remove the other
4. Leave all other cells unchanged
"""
