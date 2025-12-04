HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: L-SHAPED PATH BETWEEN TWO MARKERS             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TWO non-zero marker cells in the input
• One marker acts as the "corner anchor" - the path bends at its column or row
• Draw an L-shaped path connecting them using a NEW connector color

PATH CONSTRUCTION:
• The path consists of: one vertical segment + one horizontal segment
• The corner of the L is at the intersection of one marker's row and the other's column
• The connector color fills all cells BETWEEN the markers (exclusive of markers themselves)
• Both original markers remain unchanged

DETERMINING THE CORNER:
• Identify which marker is "above/below" and which is "left/right"
• The L-path goes: from one marker vertically to the corner row, then horizontally to the other marker
• The corner position is at (row of one marker, column of the other marker)

YOUR OUTPUT MUST:
1. Locate both marker positions
2. Determine the corner point of the L
3. Draw vertical segment from one marker toward the corner
4. Draw horizontal segment from corner toward the other marker
5. Use a distinct connector color for the path (not the marker colors)
"""
