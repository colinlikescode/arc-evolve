HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CORNER MARKERS → CENTRAL BLOCK ASSEMBLY                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the small rectangular ANCHOR BLOCK (uniform non-zero color, typically 2x2)
• Find the 4 isolated MARKER CELLS (single non-zero cells, different from anchor)
• Each marker's position relative to the anchor determines its quadrant:
  - Markers LEFT of anchor AND ABOVE anchor → top-left position
  - Markers RIGHT of anchor AND ABOVE anchor → top-right position
  - Markers LEFT of anchor AND BELOW anchor → bottom-left position
  - Markers RIGHT of anchor AND BELOW anchor → bottom-right position
• Replace the anchor block with a 2x2 block containing the 4 marker colors in their respective positions
• Clear everything else to background (zero)

KEY INSIGHT:
The scattered markers act as "corner indicators" - their spatial relationship to the central anchor block determines where their colors appear in the final 2x2 output block.
"""
