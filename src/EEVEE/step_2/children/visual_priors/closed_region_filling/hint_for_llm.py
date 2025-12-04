HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CLOSED REGION FILLING PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains shapes drawn with a "boundary" color on a background
• Identify regions that are COMPLETELY ENCLOSED by the boundary color
• Fill the interior of closed regions with a secondary "fill" color
• Leave open/incomplete shapes unfilled

KEY CONCEPTS:
• A closed region has no gaps - boundary cells completely surround interior cells
• Interior = background-colored cells that cannot "escape" to the grid edge without crossing a boundary
• Think of it like flood-fill: if you pour water inside, it stays contained
• Small enclosed areas (even single cells between boundaries) should be filled

YOUR APPROACH MUST:
1. Find all boundary-color cells (the non-background color in input)
2. Identify which background cells are enclosed (cannot reach grid edge)
3. Fill enclosed background cells with the fill color
4. Preserve all boundary cells unchanged
"""
