HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ROW-BASED COLOR PROPAGATION PATTERN           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There is a "key column" containing color values that vary by row
• There is a "placeholder color" used to mark regions that need to be filled
• The placeholder color is distinct from both the background and key colors

HOW TO TRANSFORM:
• For each cell in the grid:
  - If the cell contains the placeholder color → replace it with the key color from that row's key column
  - If the cell contains any other value → keep it unchanged

KEY OBSERVATIONS:
• The key column typically has non-zero, non-placeholder values
• The placeholder color appears in contiguous regions/blocks
• Each row's placeholder cells all become the same color (the row's key)
• Background cells (zeros) stay as background

YOUR APPROACH:
1. Identify the key column (column with varying non-placeholder colors)
2. Identify the placeholder color (consistent color used in fillable regions)
3. For each row, find its key color from the key column
4. Replace all placeholder cells in that row with the row's key color
"""
