HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RANK LINE SEGMENTS BY LENGTH → ASSIGN COLORS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains multiple line segments (horizontal or vertical) of a single marker color
• Each segment is a contiguous run of non-zero cells in one direction
• Segments are RANKED by their LENGTH (number of cells)

COLOR ASSIGNMENT BY RANK:
• LONGEST segment → first rank color
• MEDIUM length segment → second rank color  
• SHORTEST segment → third rank color

KEY OBSERVATIONS:
• The position of each segment stays the same
• Only the color changes based on relative length
• If segments have equal length, consider their position or other ordering

YOUR APPROACH:
1. Find all distinct line segments (contiguous non-zero cells in a row or column)
2. Calculate the length of each segment
3. Rank segments from longest to shortest
4. Assign the appropriate rank-based color to each segment
5. Preserve segment positions, replace marker color with rank color
"""
