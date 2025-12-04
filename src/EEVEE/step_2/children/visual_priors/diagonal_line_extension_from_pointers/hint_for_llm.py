HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL LINE EXTENSION FROM POINTER CELLS    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a central shape (typically a 2x2 block) plus isolated "pointer" cells
• Each isolated cell indicates a diagonal direction relative to the central shape
• The output EXTENDS diagonal lines from each pointer cell, continuing in the same diagonal direction (away from the central shape) until reaching the grid edge

HOW TO IDENTIFY THE DIRECTION:
• Find the central compact shape (the 2x2 block)
• Find isolated single cells of the same color
• Each isolated cell sits diagonally from the main shape
• The diagonal direction is: FROM the central shape THROUGH the pointer cell
• Continue that diagonal line beyond the pointer cell to the grid boundary

YOUR APPROACH:
1. Identify the main compact shape and its center/anchor point
2. Find all isolated single cells (same color, not part of main shape)
3. For each isolated cell, determine which diagonal direction it indicates
4. Draw a diagonal line from that cell, extending in the same direction until hitting the grid edge
5. Keep all original cells in place
"""
