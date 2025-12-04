HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A HEADER ROW EXPANSION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The first row contains a sequence of distinct colors (the "header")
• The second row is a uniform separator row (keep it unchanged)
• All rows below the separator are empty/zero in the input

TO FILL THE EMPTY REGION:
• Read the colors from the header row left-to-right
• For each empty row below the separator:
  - Fill the ENTIRE row with a single color from the header sequence
  - Cycle through the header colors in order (first color, second color, etc.)
  - When you reach the end of the header sequence, loop back to the first color
• Continue until all empty rows are filled

KEY INSIGHT:
• Each header color "expands" into a full horizontal row
• The header defines the repeating color sequence
• The expansion cycles as many times as needed to fill the available space
"""
