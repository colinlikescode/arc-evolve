HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MATCHING ENDPOINT LINE FILL PATTERN           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Examine each row that has non-zero cells at both the leftmost and rightmost positions
• Compare the color at the left edge with the color at the right edge
• IF THEY MATCH: Fill the entire row (all cells between and including endpoints) with that color
• IF THEY DIFFER: Leave the row unchanged

KEY INSIGHT:
• Only rows with IDENTICAL endpoint colors get the horizontal line fill
• Rows with different endpoint colors remain as-is
• Rows without endpoints (all zeros) stay unchanged

YOUR APPROACH:
1. For each row, check if there are non-zero values at both column 0 and the last column
2. If those two values are equal, fill the entire row with that value
3. Otherwise, keep the row unchanged
"""
