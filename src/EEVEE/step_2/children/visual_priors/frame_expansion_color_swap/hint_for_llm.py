HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FRAME EXPANSION WITH COLOR ROLE SWAP          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input has a framed rectangle: OUTER_COLOR frames INNER_COLOR
• The pattern expands outward by the size of the inner region
• Colors swap roles in the expansion:
  - INNER_COLOR becomes the NEW outer frame
  - OUTER_COLOR fills the expanded interior
  - The original pattern remains at center with colors swapped

CONCEPTUALLY:
• Find the two non-background colors (frame color and core color)
• Measure the inner region dimensions (this determines expansion size)
• Expand the bounding box by that amount in all directions
• In the expanded pattern:
  - New outer ring = original inner color
  - New inner fill = original frame color  
  - Center preserves original structure with swapped colors

The result is like adding one "layer" to a nested frame structure.
"""
