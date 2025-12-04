HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL LINE LENGTH COMPARISON PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains multiple vertical columns of a marker color
• Each column has a different length (number of consecutive marked cells)
• Count the length of each vertical line from its start to the bottom

OUTPUT CONSTRUCTION:
• Find the LONGEST vertical column → mark it with the "primary" output color
• Find the SHORTEST vertical column → mark it with the "secondary" output color
• Remove ALL other columns (set to background)
• Preserve the original positions and lengths of the two extreme columns

KEY INSIGHT:
• This is an EXTREMA DETECTION task
• You're finding MAX and MIN among parallel vertical structures
• The two extremes get distinct colors; everything else disappears
"""
