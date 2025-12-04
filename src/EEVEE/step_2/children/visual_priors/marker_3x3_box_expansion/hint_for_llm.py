HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: 3x3 BOX EXPANSION AROUND MARKER CELLS         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the "marker" color - the one that appears multiple times as isolated cells
• Identify other non-zero cells as "static" elements that don't change
• For EACH marker cell at position (r, c):
  - Draw a 3x3 box centered on (r, c) using a "fill" color
  - Keep the marker cell at the center
  - The fill color is typically one not prominently used in the input
• Static cells (other non-zero colors) remain unchanged and are NOT overwritten
• Respect grid boundaries - truncate the 3x3 if it would go out of bounds

KEY OBSERVATIONS:
• The marker color is the one that triggers expansion (often appears multiple times)
• Static/blocker cells of other colors remain in place
• The 3x3 fill creates a border around each marker without disturbing other elements
"""
