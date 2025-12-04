HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL PATTERN EXTENSION PUZZLE           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output width = 2 × input width
• Output height = input height (unchanged)
• Background rows (all zeros) → remain as zeros, doubled in width
• Pattern rows (non-zero content) → extend horizontally by continuing the repeating pattern

KEY INSIGHT:
• The non-zero rows contain a REPEATING PATTERN (periodic sequence)
• To extend: continue the pattern cyclically for the additional columns
• Each pattern row has a period/cycle - identify it and tile accordingly

HOW TO EXTEND PATTERN ROWS:
• For each column index c in the output: output[row][c] = input[row][c % input_width]
• This continues the periodic pattern seamlessly

STRUCTURE:
Input (H × W)  →  Output (H × 2W)
Pattern rows are tiled/extended horizontally
Background rows remain as background
"""
