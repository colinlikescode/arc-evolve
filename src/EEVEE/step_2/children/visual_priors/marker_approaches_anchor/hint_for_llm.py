HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER MOVES ONE STEP TOWARD ANCHOR           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains exactly TWO non-zero colored cells
• One cell acts as a FIXED ANCHOR (does not move)
• The other cell acts as a MOVER (shifts one step toward the anchor)
• The MOVER advances by one cell along the path toward the ANCHOR

HOW TO IDENTIFY WHICH IS WHICH:
• One specific color type always stays fixed (the anchor)
• The other color type always moves (the mover)
• Observe which color moved in training examples to identify roles

MOVEMENT DIRECTION:
• The mover shifts one step in the direction of the anchor
• If diagonal: move one step diagonally toward anchor
• If same row/column: move one step along that axis toward anchor
• Movement is exactly ONE cell closer (reducing distance by 1 in each relevant dimension)

YOUR CODE MUST:
1. Find the two non-zero cells and their colors
2. Determine which color is the mover vs anchor (from pattern observation)
3. Move the mover one step toward the anchor
4. Keep the anchor in its original position
"""
