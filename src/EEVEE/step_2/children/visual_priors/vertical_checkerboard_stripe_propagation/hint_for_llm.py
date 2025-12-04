HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL CHECKERBOARD STRIPE PROPAGATION      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input has seed cells (non-zero values) ONLY in the first row
• Each seed cell propagates downward creating a checkerboard stripe pattern
• The pattern alternates by row parity:
  - EVEN rows (0, 2, 4...): color appears at the SEED COLUMN position
  - ODD rows (1, 3, 5...): color appears at SEED COLUMN ± 1 (left and right neighbors)

VISUAL PATTERN (for a seed at column C):
Row 0:  ...C...     (original seed position)
Row 1:  .C.C.       (left and right of seed)
Row 2:  ...C...     (back to center)
Row 3:  .C.C.       (left and right again)
...and so on...

KEY OBSERVATIONS:
• Each seed operates independently
• Multiple seeds create overlapping stripe patterns
• Grid dimensions remain unchanged
• Only positions within grid bounds are filled
"""
