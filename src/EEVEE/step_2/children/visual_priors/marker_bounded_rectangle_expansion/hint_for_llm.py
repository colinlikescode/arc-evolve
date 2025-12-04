HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-BOUNDED RECTANGLE EXPANSION            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the small rectangular shape (the "inner frame") - uses one non-background color
• Find exactly 4 marker cells (a different secondary color) - these define corner boundaries
• The markers indicate where a LARGER outer rectangle should be drawn

HOW TO CONSTRUCT THE OUTPUT:
• Keep the original small shape exactly where it is
• Keep all 4 markers in their original positions
• Draw a NEW larger rectangle using the SAME color as the inner shape
• The outer rectangle's edges pass through the row/column positions just inside the markers
• The outer rectangle is a hollow frame (only the perimeter is filled)

SPATIAL RELATIONSHIP:
• Each marker sits just outside one corner of the new outer rectangle
• The outer rectangle is positioned so markers are adjacent to its corners
• The inner shape remains centered/unchanged within the larger frame
"""
