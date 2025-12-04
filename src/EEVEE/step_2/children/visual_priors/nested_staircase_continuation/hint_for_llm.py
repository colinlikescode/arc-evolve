HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NESTED STAIRCASE CONTINUATION PATTERN         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a partial "staircase" or nested L-shape pattern
• The output CONTINUES this staircase pattern to fill the entire grid
• The non-zero cells define a repeating step structure
• Extend the pattern by identifying the step increment/direction

KEY OBSERVATIONS:
• Find the "spine" or longest edge of the shape
• Identify the step pattern (how the stairs grow/shrink)
• Continue the alternating pattern to fill all remaining space
• Use a secondary fill color for the spaces between steps
• The original shape's cells keep their original color

THE OUTPUT HAS:
• Original non-zero color: forms the staircase lines/edges
• Fill color: fills the spaces between staircase steps
• The entire grid is covered with no background remaining
"""
