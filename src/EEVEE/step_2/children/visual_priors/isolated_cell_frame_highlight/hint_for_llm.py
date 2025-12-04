HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ISOLATED CELL DETECTION WITH FRAME OUTPUT     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the ONE cell in the input that is completely isolated (all 8 neighbors are zero/background)
• Create an output grid filled entirely with background color
• At the position of the isolated cell, draw a 3x3 block:
  - The CENTER cell keeps the isolated cell's original color
  - The 8 SURROUNDING cells use a "frame color" (look for a consistently used color in inputs, often appearing in structured patterns)

KEY INSIGHT:
• Most non-zero cells in the input have at least one non-zero neighbor
• Exactly ONE cell will have ALL 8 neighbors equal to zero
• This unique isolated cell becomes the center of the output's 3x3 framed region

The frame color appears to be consistent across examples - identify which color serves as the "marker" or "frame" color by examining what color is used for the border in the outputs.
"""
