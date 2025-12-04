HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-GUIDED LINE PROJECTION PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• There is a SOURCE PATTERN: a row or column with non-background cells of one color
• There are MARKERS: cells of a different color along a perpendicular axis
• The source pattern is EXTENDED/REPEATED through the grid
• At each MARKER position, the pattern SHIFTS by one position in the marker's direction

KEY OBSERVATIONS:
• The markers define "zones" or segments in the grid
• Within each zone, the pattern is copied vertically or horizontally
• When crossing a marker, the pattern shifts (slides) by one cell
• Markers themselves remain unchanged in the output

YOUR APPROACH:
1. Identify the source pattern (row or column with one non-background color)
2. Identify the markers (different color, perpendicular to source)
3. For each zone between markers, extend the pattern
4. Apply cumulative shift based on how many markers have been passed
"""
