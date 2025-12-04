HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DUAL-REGION COMPARISON PUZZLE                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is split into TWO equal halves (top and bottom)
• Each half contains a pattern made with a different non-zero color
• Compare corresponding cells between the two halves

COMPARISON LOGIC:
• For each position (row, col) in the output:
  - Check if the TOP half has background (zero) at that position
  - Check if the BOTTOM half has background (zero) at that position
  - If BOTH halves have background → mark with a NEW color in output
  - Otherwise → output is background (zero)

CONCEPTUALLY:
• Find where NEITHER pattern occupies a cell
• The output highlights the "empty intersection" of both patterns
• Output uses a color different from both input pattern colors
"""
