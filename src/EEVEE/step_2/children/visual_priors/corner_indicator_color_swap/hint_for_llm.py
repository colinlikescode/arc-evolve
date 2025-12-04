HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COLOR REPLACEMENT WITH CORNER INDICATOR       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There are exactly TWO non-zero colors in the input
• One color forms the main pattern/shape
• The other color appears as a SINGLE isolated cell in a corner (the "indicator")

TO SOLVE:
1. Identify the isolated single-cell color in a corner → this is the REPLACEMENT color
2. Identify the other non-zero color → this is the PATTERN color
3. In the output:
   - Replace ALL cells of the pattern color with the replacement color
   - Set the corner indicator cell to background (zero)
   - Keep all background cells unchanged

The shape/pattern is PRESERVED, only the color changes.
"""
