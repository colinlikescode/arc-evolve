HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL TRAILS FROM PAIRED BLOCKS            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two colored blocks exist in the input - keep both in place
• Determine which block is "upper-left" vs "lower-right" based on their positions
• From the upper-left block: draw a diagonal trail of single pixels extending toward the top-left corner (up-left direction)
• From the lower-right block: draw a diagonal trail of single pixels extending toward the bottom-right corner (down-right direction)

TRAIL DETAILS:
• Each trail starts from the corner of the block nearest to the target corner
• Trail pixels are placed diagonally (row-1, col-1 for up-left; row+1, col+1 for down-right)
• Continue until reaching the grid boundary
• Each trail uses the same color as its source block

DETERMINING BLOCK ROLES:
• Compare the blocks' positions (e.g., by top-left corner coordinates)
• The block with smaller row+column sum is the "upper-left" block
• The other is the "lower-right" block
"""
