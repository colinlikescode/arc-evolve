HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: XOR COMPARISON OF TWO STACKED PATTERNS        ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• Input is divided into THREE parts by a horizontal separator row
• TOP region: contains pattern A using one non-background color
• SEPARATOR: a single row of uniform color (divider)
• BOTTOM region: contains pattern B using a different non-background color

THE TRANSFORMATION RULE:
• Output size matches the size of each region (excluding separator)
• For each cell position, compare top region vs bottom region:
  - If ONLY the top has a non-background cell → mark in output
  - If ONLY the bottom has a non-background cell → mark in output
  - If BOTH have non-background cells → output is background
  - If NEITHER has non-background → output is background

This is an XOR (exclusive or) operation on the two patterns!

OUTPUT MARKING:
• Use a new marker color (different from both input colors)
• Mark cells where exactly ONE of the two regions has content
"""
