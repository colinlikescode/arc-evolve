HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SPLIT-AND-COMPARE / XOR BETWEEN HALVES       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A divider line (single distinct color column) splits the input into LEFT and RIGHT halves
• The output size matches ONE half (excluding the divider column)
• Each half contains cells with two possible values: a "background" color and a "marker" color

COMPARISON LOGIC:
• For each row, compare corresponding cells from left half and right half
• If BOTH sides have the marker color (non-background) → output is background (black/zero)
• If BOTH sides have the background color → output is background (black/zero)  
• If sides DIFFER (one has marker, other has background) → output shows a HIGHLIGHT color

This is essentially an XOR operation:
• Same values on both sides → no highlight
• Different values → highlight that cell

YOUR APPROACH:
1. Find the divider column (the column with a unique single color)
2. Extract left region (before divider) and right region (after divider)
3. Compare cell-by-cell: mark with highlight color where one side has the "zero/black" value and the other has the "background" value
"""
