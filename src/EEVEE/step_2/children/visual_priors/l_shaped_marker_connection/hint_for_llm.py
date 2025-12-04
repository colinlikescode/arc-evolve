HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: L-SHAPED LINE EXTENSION BETWEEN MARKER PAIRS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find TWO distinct marker colors (not background, not noise/scattered color)
• Each marker appears as a small segment (typically 2 adjacent cells)
• Draw L-shaped lines connecting the two marker segments

HOW THE L-SHAPE WORKS:
• From each marker segment, extend a line in the direction of its orientation
• Continue until reaching the row or column of the OTHER marker
• Turn 90 degrees and continue toward the other marker
• The result forms an L or corner shape using ONE of the marker colors

IDENTIFYING MARKERS:
• Markers are small, intentional clusters (2 cells, adjacent)
• The scattered/noise color (appears randomly throughout) is NOT a marker
• Background color (most common, typically 0) is NOT a marker
• Look for exactly 2 rare colors that form deliberate small patterns

THE L-EXTENSION:
• One marker color is used to draw the connecting L-shape
• Extend from the marker's endpoint in its natural direction
• The corner of the L aligns with the other marker's position
"""
