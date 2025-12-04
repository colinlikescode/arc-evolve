HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BOUNDING BOX EXTRACTION PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find ALL non-zero (non-background) cells in the input grid
• Determine the minimal bounding rectangle that encloses all these cells
• Extract that rectangular region exactly as the output

KEY OBSERVATIONS:
• The output dimensions = (max_row - min_row + 1) × (max_col - min_col + 1)
• Where min/max row/col are the boundaries of non-zero cells
• The pattern inside the bounding box is preserved EXACTLY
• Both non-zero AND zero cells within the bounding box are kept

YOUR APPROACH:
1. Scan the input to find all positions with non-zero values
2. Find the minimum and maximum row and column indices
3. Extract the rectangular slice from min_row:max_row+1, min_col:max_col+1
4. That extracted region IS the output
"""
