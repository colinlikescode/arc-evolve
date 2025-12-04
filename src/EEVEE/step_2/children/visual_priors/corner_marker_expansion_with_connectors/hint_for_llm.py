HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CORNER MARKER EXPANSION WITH CONNECTORS       ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• 4 non-zero cells at corners of a rectangle
• Two distinct colors, each appearing twice (diagonally opposite)

THE TRANSFORMATION RULE:
• Each corner marker becomes a 3x3 block
• The 3x3 block's BORDER uses the OPPOSITE corner's color
• The 3x3 block's CENTER uses the ORIGINAL color at that position
• A connector color (new, not in input) links the corners:
  - Horizontal dotted lines between corners on the same row
  - Vertical lines between corners in the same column

VISUAL PATTERN:
If corners are at positions (r1,c1), (r1,c2), (r2,c1), (r2,c2):
- Each becomes a 3x3 centered on that position
- Colors swap: border = diagonal partner's color, center = original
- Connector marks appear between pairs at regular intervals
"""
