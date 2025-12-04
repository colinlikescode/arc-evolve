HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECT REGION WITH MAXIMUM ACCENT COLOR       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple distinct regions of the same size, separated by background cells
• Each region contains patterns made of two non-zero colors: a dominant color and an accent color
• Identify all candidate regions (same-sized rectangular blocks with non-zero content)
• For each region, count occurrences of the accent/minority color
• The output is the region that has the MAXIMUM count of the accent color

HOW TO IDENTIFY:
1. Find all distinct rectangular regions containing non-zero values
2. Determine which non-zero color is the "accent" (less frequent overall)
3. Count the accent color occurrences in each region
4. Select and output the region with the highest accent color count

The output is simply one of the input regions extracted directly - no transformation of the pattern itself.
"""
