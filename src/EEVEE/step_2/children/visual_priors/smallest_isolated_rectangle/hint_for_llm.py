HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  FIND THE SMALLEST ISOLATED RECTANGLE                    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple colored rectangular regions
• Some rectangles OVERLAP or TOUCH other colored regions
• Some rectangles are COMPLETELY ISOLATED (only bordered by background)
• Find the rectangle that is:
  1. NOT overlapping or adjacent to any other non-background region
  2. The SMALLEST among all isolated rectangles

OUTPUT:
• Extract that isolated rectangle as the output
• The output is a solid rectangle filled with that region's color
• Output dimensions match the isolated rectangle's size

HOW TO IDENTIFY "ISOLATED":
• A rectangle is isolated if expanding its bounding box by 1 cell in all directions contains ONLY background color (besides the rectangle itself)
• Rectangles that share edges or overlap with other colored regions are NOT isolated
"""
