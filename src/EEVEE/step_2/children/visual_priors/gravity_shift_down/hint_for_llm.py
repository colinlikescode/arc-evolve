HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A GRAVITY/DOWNWARD SHIFT PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The entire non-zero pattern shifts DOWN by exactly ONE ROW
• The pattern shape, colors, and relative positions are preserved
• The top row of the output becomes all background (zeros)
• Cells that would shift "off" the bottom are lost (but typically the bottom row is empty in input)

CONCEPTUALLY:
• Think of gravity pulling the pattern down one step
• Copy each row to the row below it
• Fill the top row with background color

YOUR APPROACH:
1. Identify all non-zero cells and their positions
2. Move each non-zero cell down by one row
3. Ensure the top row is filled with zeros
4. Preserve the original color values
"""
