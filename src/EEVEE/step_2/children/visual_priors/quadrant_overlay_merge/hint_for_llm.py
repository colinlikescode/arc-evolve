HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A QUADRANT OVERLAY PUZZLE             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is divided into 4 equal quadrants (top-left, top-right, bottom-left, bottom-right)
• Each quadrant contains a sparse pattern with its own distinct color
• The output size equals one quadrant's size

FOR EACH POSITION (r, c) IN THE OUTPUT:
• Check the corresponding position in all four quadrants
• If a quadrant has a non-zero value at that position, its color contributes to the output
• When overlaying, non-zero values from any quadrant appear in the output
• If multiple quadrants have non-zero values at the same position, use a consistent selection rule (e.g., priority based on quadrant position)

CONCEPTUALLY:
• Think of each quadrant as a transparent layer with colored marks
• Stack all four layers on top of each other
• The output shows the combined result of all layers
"""
