HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME-PATTERN OVERLAY PUZZLE                  ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT CONTAINS TWO SEPARATE STRUCTURES:
1. A FRAME: 4 line segments forming a rectangle (top, bottom, left, right - each a different color)
2. A PATTERN: A shape made of a single distinct color

THE TRANSFORMATION RULE:
• The output size matches the frame's interior dimensions plus the border
• The frame forms the outer edge of the output
• The pattern is placed inside the frame
• For each cell in the pattern: extend the corresponding frame edge colors inward
  - Cells in the pattern's column range get filled with left/right edge colors
  - Cells in the pattern's row range get filled with top/bottom edge colors
• The pattern color remains where it originally appears
• Frame colors "propagate" inward based on pattern cell positions

CONCEPTUALLY:
• Think of projecting each pattern cell toward all 4 edges
• The frame colors fill the space between the pattern and their respective edges
"""
