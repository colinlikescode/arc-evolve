HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND AND MARK SOLID RECTANGULAR REGIONS       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has two colors: a dominant color and a secondary (minority) color
• Search for solid rectangular regions (e.g., 3x3 blocks) filled ENTIRELY with the secondary color
• These "pure" blocks contain ONLY the secondary color - no dominant color cells inside
• Replace these solid rectangular regions with a NEW marker color
• Everything else in the grid stays exactly the same

HOW TO IDENTIFY TARGET REGIONS:
• Look for rectangular areas where ALL cells are the secondary/minority color
• The size appears to be 3x3 in the examples
• Multiple such regions may exist - mark ALL of them

KEY INSIGHT:
• Only SOLID blocks get marked - partial or irregular shapes are ignored
• The marker color does not appear in the input at all
"""
