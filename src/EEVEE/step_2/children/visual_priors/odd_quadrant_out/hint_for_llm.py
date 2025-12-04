HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND THE ODD QUADRANT OUT                     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is divided into 4 quadrants by separator rows/columns (all zeros)
• Three quadrants are IDENTICAL, one quadrant is DIFFERENT
• The output is the UNIQUE/DIFFERENT quadrant

HOW TO IDENTIFY:
• Find the separator row(s) and column(s) - typically all background color
• Extract the four quadrants from the corners
• Compare all quadrants to find which one differs from the majority
• Output that unique quadrant

THE OUTPUT IS THE "ODD ONE OUT" - the quadrant that doesn't match the others.
"""
