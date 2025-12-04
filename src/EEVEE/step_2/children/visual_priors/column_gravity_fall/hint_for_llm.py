HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS PUZZLE HAS COLUMN-WISE GRAVITY           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each column is processed independently
• All non-zero cells in a column "fall" to the bottom
• The relative order of non-zero cells within each column is preserved
• Background (zero) cells fill the remaining space at the top

CONCEPTUAL MODEL:
Think of gravity pulling colored blocks downward:
- Colored cells drop until they hit the bottom or another colored cell
- Empty space rises to the top
- Columns do not interact with each other

YOUR APPROACH MUST:
1. Process each column separately
2. Extract all non-zero values from the column (preserving top-to-bottom order)
3. Place them at the bottom of that column in the output
4. Fill the remaining top positions with zeros
"""
