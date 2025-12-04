HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MIDDLE ROW ALTERNATING PATTERN                ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all solid rectangular regions (3 rows tall, filled with non-background color)
• Keep the FIRST row and LAST row of each rectangle unchanged
• In the MIDDLE row: apply alternating pattern starting from the first cell
  - Keep original color at even positions (0, 2, 4, ...)
  - Replace with background at odd positions (1, 3, 5, ...)

VISUAL PATTERN:
Input rectangle:    Output rectangle:
█ █ █ █ █ █ █       █ █ █ █ █ █ █   (top row: unchanged)
█ █ █ █ █ █ █  →    █ ○ █ ○ █ ○ █   (middle row: alternating)
█ █ █ █ █ █ █       █ █ █ █ █ █ █   (bottom row: unchanged)

KEY INSIGHT:
• Only 3-row-tall rectangles are affected
• The alternating pattern uses the rectangle's starting column position
• Each rectangle is processed independently
"""
