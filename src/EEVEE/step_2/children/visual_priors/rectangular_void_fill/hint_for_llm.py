HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A VOID DETECTION AND FILL PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input has a scattered pattern of non-zero cells on a background
• There exists a large rectangular region of ONLY background (zero) cells
• This "void" represents missing or empty space in the pattern

YOUR TASK:
1. Identify the rectangular region that is entirely background color
2. This void is bounded by rows/columns where the pattern exists on both sides
3. Fill this entire rectangular void with a highlight color (typically green/3)
4. Leave all other cells unchanged

KEY INSIGHT:
• The void is the maximal rectangle where ALL cells are background
• It appears as a "hole" in the pattern that spans both horizontally and vertically
• The highlight color marks this detected void region

LOOK FOR:
• Rows that are entirely or mostly background in a contiguous block
• Columns that are entirely or mostly background in a contiguous block
• The intersection of these empty rows and columns defines the void
"""
