HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ROW-COLUMN INTERSECTION FILLING PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two "axes" define the pattern:
  - COLUMN markers: non-zero cells in the first row (defines which columns)
  - ROW markers: non-zero cells in the last column (defines which rows)
• For each ROW that has a marker in the last column:
  - Fill all cells in that row that correspond to COLUMN positions marked in the first row
  - Use a different fill color (not the original marker color)
• The original markers (first row and last column) are PRESERVED unchanged
• Only the interior intersection cells receive the new fill color

CONCEPTUAL APPROACH:
1. Identify column positions from first-row markers
2. Identify row positions from last-column markers
3. At each (marked_row, marked_column) intersection, place the fill color
4. Keep original marker cells in their original color
"""
