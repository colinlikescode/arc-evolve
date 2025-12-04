HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKERS EXTEND VERTICALLY TO BOUNDARIES       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• A horizontal divider line splits the grid into upper and lower regions
• Two distinct marker colors exist (call them Color A and Color B)
• Color A markers: extend TOWARD the divider line
  - Draw a vertical line from the marker to the divider (not crossing it)
• Color B markers: extend AWAY from the divider line
  - Draw a vertical line from the marker to the grid edge (top or bottom)

DIRECTION LOGIC:
• In the UPPER region: "toward divider" = downward, "away" = upward
• In the LOWER region: "toward divider" = upward, "away" = downward

YOUR APPROACH MUST:
1. Find the horizontal divider row (the row filled with a single uniform color)
2. Identify the two marker colors (non-zero, non-divider colors)
3. Determine which color extends toward vs away from the divider
4. For each marker, extend it vertically in the appropriate direction
"""
