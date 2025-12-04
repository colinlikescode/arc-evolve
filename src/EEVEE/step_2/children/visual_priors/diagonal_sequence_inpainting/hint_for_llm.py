HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIAGONAL SEQUENCE INPAINTING PUZZLE           ║
╚══════════════════════════════════════════════════════════════╝

THE UNDERLYING PATTERN:
• The grid follows a diagonal sequence: value = f(row + col)
• Each diagonal (where row + col is constant) has the same value
• The sequence cycles through N distinct non-zero values
• Moving right or down increments the value (with wraparound)

THE TRANSFORMATION RULE:
• Zero cells are MASKS hiding the true pattern
• The output RESTORES the complete diagonal sequence
• For each cell: output[row][col] = ((row + col) mod period) + start_value

HOW TO SOLVE:
1. Identify the period N by examining non-zero values (find the cycle length)
2. Determine the starting value at position (0,0) from a non-masked cell
3. For every cell: compute value based on (row + col) mod N
4. The formula ensures diagonal consistency across the entire grid

KEY INSIGHT: The pattern is fully determined by position - use any non-masked cell to calibrate, then fill all cells using the diagonal formula.
"""
