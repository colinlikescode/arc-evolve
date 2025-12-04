HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL DIVIDER MERGE PUZZLE               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the horizontal divider line (a full-width row of uniform non-background color)
• This divider splits the input into an UPPER region and a LOWER region
• Remove the divider row entirely
• OVERLAY the two regions on top of each other:
  - The output has the same dimensions as each region
  - For each cell position, combine values from both regions
  - Non-background cells from either region appear in the output
  - If both regions have non-background at the same position, both appear (they typically don't conflict)

KEY INSIGHT:
• The divider acts as a "fold line" - imagine folding the grid along this line
• The upper and lower halves merge together, preserving all non-background content from both
• Background (zero) cells are transparent - they don't overwrite colored cells from the other region
"""
