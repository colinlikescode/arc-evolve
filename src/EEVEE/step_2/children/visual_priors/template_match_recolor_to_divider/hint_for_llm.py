HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE MATCHING WITH DIVIDER RECOLORING     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has DIVIDER LINES made of a specific color forming a bounded region
• The TOP-LEFT region (bounded by dividers) contains a TEMPLATE SHAPE
• Scan all other shapes in the grid
• Any shape that MATCHES the template's geometric form (same relative cell pattern, possibly rotated/reflected) gets RECOLORED to the DIVIDER COLOR
• Non-matching shapes remain unchanged

HOW TO IDENTIFY COMPONENTS:
• DIVIDER: Look for a color forming horizontal AND vertical lines that create a bounded corner region
• TEMPLATE: The non-background, non-divider shape inside that bounded region
• CANDIDATES: All other distinct colored shapes outside the template region

MATCHING CRITERIA:
• Compare the relative positions of cells in each shape
• Account for rotations (90°, 180°, 270°) and reflections
• Same shape = same pattern of filled cells relative to each other

OUTPUT: Copy input, but recolor all template-matching shapes to the divider color
"""
