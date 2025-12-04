HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TWO-POINT PERIODIC LINE EXTENSION PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero cells in the input - they define a repeating pattern
• Determine the AXIS of extension based on point arrangement:
  - If points share similar column positions → extend as HORIZONTAL lines (fill rows)
  - If points share similar row positions → extend as VERTICAL lines (fill columns)
• Calculate the PERIOD: the distance between the two points along the perpendicular axis
• Starting from each original point's position, fill entire lines with that color
• Repeat the two-line pattern periodically to fill the remaining grid

KEY INSIGHT:
• The two points act as "seeds" that define both the colors AND the spacing
• One point's position sets the first line, the other sets the second line
• This two-line unit then tiles/repeats across the entire grid dimension
• Lines extend fully across the grid width (for horizontal) or height (for vertical)
"""
