HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A GRAVITY/DROP TO SURFACE PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the "ground" row (typically a filled horizontal line near the bottom)
• Find special marker cells that are positioned ABOVE the ground
• These markers have indicator cells directly above them (different color)

THE GRAVITY EFFECT:
• The indicator cells "fall" down to the ground level
• They replace the ground color at their respective column positions
• Their original positions become background (empty)
• Supporting/marker cells shift down by one row (filling where indicators were)

CONCEPTUALLY:
• Think of it as dropping objects onto a floor
• Each object falls straight down in its column
• The column position is preserved, only the row changes
• Objects come to rest ON the ground line (become part of it)
"""
