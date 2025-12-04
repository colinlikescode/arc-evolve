HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ANCHOR BLOCK LINE EXTENSION PATTERN           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the small rectangular block (anchor) - typically 2x2
• Identify scattered single-cell markers of various colors
• For each marker that aligns horizontally or vertically with an edge of the anchor:
  - Draw a line FROM the anchor's edge TO the marker
  - The line uses the MARKER'S color
  - Fill all cells between the anchor edge and the marker

KEY OBSERVATIONS:
• Lines extend outward from the anchor block's boundaries
• Only markers that share a row/column with the anchor's edges get connected
• The connecting line takes the color of the destination marker
• Original markers and the anchor block remain unchanged
• Lines stop at the anchor edge, not inside it
"""
