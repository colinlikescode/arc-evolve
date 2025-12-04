HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: COMPARE HOLLOW RECTANGLES BY INTERIOR SIZE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple hollow rectangular frames, each in a different color
• Each rectangle has a border of colored cells surrounding a hollow interior (background cells)
• Compare the INTERIOR SIZE of each rectangle (the hollow part)
• The rectangle with the SMALLER interior (more "filled" or "thicker" walls relative to size) is the answer
• Output a 2×2 grid filled entirely with the color of that "winner" rectangle

HOW TO IDENTIFY THE WINNER:
• Calculate the ratio of border cells to interior cells for each rectangle
• OR compare the absolute interior dimensions
• The rectangle with proportionally less empty space inside wins
• Output its color as a solid 2×2 block

KEY INSIGHT:
The "more solid" or "more filled" rectangle determines the output color.
"""
