HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CONNECT MARKER PAIRS WITH LINES               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has sparse MARKER cells on a background
• Find pairs of markers that share the SAME ROW → draw horizontal line between them
• Find pairs of markers that share the SAME COLUMN → draw vertical line between them
• Use a SECONDARY COLOR (different from marker and background) for the lines
• Lines fill cells BETWEEN the two markers, not over the markers themselves
• Original markers remain unchanged

KEY OBSERVATIONS:
• Only connect markers that are on the EXACT same row or EXACT same column
• Multiple pairs can exist - each valid pair gets connected
• When markers share both row AND column with different partners, both lines are drawn
• Lines do NOT extend beyond the marker positions

YOUR APPROACH:
1. Identify all marker cell positions
2. For each row: if exactly 2 markers exist, fill between them with secondary color
3. For each column: if exactly 2 markers exist, fill between them with secondary color
4. Preserve original marker positions
"""
