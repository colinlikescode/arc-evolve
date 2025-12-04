HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CROSS REPOSITIONING BY MARKER LOCATION        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a CROSS (vertical + horizontal line) made of one color
• A MARKER color appears in a specific region (edge/corner cells)
• The marker indicates the TARGET QUADRANT for the cross intersection

HOW TO SOLVE:
1. Identify the cross color (forms both a full row and full column)
2. Find the marker color (secondary color, typically on an edge)
3. Count marker positions to determine target quadrant/location
4. The number of marker cells indicates the new position for the intersection:
   - Count markers in each row → new row for horizontal line
   - Count markers in each column → new column for vertical line
5. Redraw the cross with intersection at the new position
6. Remove all marker cells (replace with background)

KEY INSIGHT: The markers "point to" where the cross intersection should move.
The cross maintains full grid span but the intersection point shifts.
"""
