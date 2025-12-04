HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SCALED BLOCK EXPANSION WITH MARKER CELL       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the MARKER: the unique single-cell color (appears exactly once)
• Identify the PATTERN COLOR: the other non-background color
• Output dimensions = input_height × input_height, input_width × input_width
• Block size = input dimensions

FOR EACH CELL in the input:
• If cell contains the PATTERN COLOR (not marker, not background):
  → Fill a block at scaled position (row × H, col × W) with that color
• Marker and background cells → leave as background in output

KEY INSIGHT:
• The marker indicates a reference point but is NOT drawn in output
• Only the pattern-colored cells get expanded into filled blocks
• Each block is the same size as the original input grid
"""
