HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A RUN-LENGTH DEDUPLICATION PUZZLE     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains repeated "stripes" (consecutive identical rows or columns)
• The output collapses each group of consecutive identical rows/columns into ONE
• This applies in BOTH dimensions:
  - Consecutive identical ROWS → keep only one representative row
  - Consecutive identical COLUMNS → keep only one representative column

HOW TO THINK ABOUT IT:
• Scan rows: if row[i] == row[i+1], they belong to the same group
• Scan columns: if col[j] == col[j+1], they belong to the same group
• Output contains exactly ONE row/column from each consecutive group

THE OUTPUT IS THE "UNIQUE SKELETON":
• Each distinct horizontal band → one row in output
• Each distinct vertical band → one column in output
• Preserves the ORDER of stripes, just removes duplicates
"""
