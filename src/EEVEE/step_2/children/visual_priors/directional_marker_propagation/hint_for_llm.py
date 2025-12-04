HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: DIRECTIONAL PATTERN PROPAGATION WITH MARKERS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the main TEMPLATE SHAPE (the largest connected pattern)
• Identify MARKER CELLS positioned in cardinal directions from the template
• Each marker indicates a direction for propagation (up/down/left/right)

FOR EACH MARKER:
• Determine which direction it points from the template
• Replicate the template shape repeatedly in that direction
• Use the MARKER'S COLOR for all the replicated copies
• Continue replicating until reaching the grid boundary
• Spacing between copies matches the template's dimensions (plus gap)

KEY DETAILS:
• The original template shape remains unchanged in place
• Each marker spawns its own series of copies in its direction
• Copies inherit the SHAPE of the template but the COLOR of the marker
"""
