HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A HORIZONTAL BAND DENOISING PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid contains horizontal bands/stripes
• Each band has a DOMINANT color (most frequent in that row region)
• Scattered "noise" cells of other colors corrupt each band
• The output CLEANS each band by filling it entirely with its dominant color

HOW TO IDENTIFY BANDS:
• Look at each row and find the most common color
• Consecutive rows with the same dominant color form a single band
• The band boundaries are where the dominant color changes

YOUR APPROACH MUST:
1. For each row, determine the most frequent (dominant) color
2. Group consecutive rows that share the same dominant color into bands
3. Fill each entire band uniformly with its dominant color
4. Preserve the vertical structure - bands stay in the same row positions

KEY INSIGHT: The noise is SPARSE - the correct band color will always be 
the MAJORITY color in each row. Simply finding the mode of each row and 
filling that row with the mode will clean the noise.
"""
