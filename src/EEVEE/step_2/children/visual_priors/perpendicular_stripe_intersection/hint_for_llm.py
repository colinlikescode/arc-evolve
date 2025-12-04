HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: PERPENDICULAR STRIPE INTERSECTION PRIORITY   ║
╚══════════════════════════════════════════════════════════════╝

THE PATTERN:
• The grid contains two perpendicular stripes of different non-background colors
• One stripe runs vertically (through certain columns)
• One stripe runs horizontally (through certain rows)
• These stripes intersect at specific cells

THE TRANSFORMATION RULE:
• Find where the vertical and horizontal stripes intersect
• At the intersection, the HORIZONTAL stripe's color takes priority
• The horizontal stripe becomes "complete" (unbroken across its full width)
• The vertical stripe remains intact everywhere EXCEPT at the intersection

HOW TO IDENTIFY EACH STRIPE:
• The vertical stripe: cells that share the same column(s) and have a consistent non-background color vertically
• The horizontal stripe: cells that share the same row(s) and have a consistent non-background color horizontally
• At intersection: replace with the horizontal stripe's color
"""
