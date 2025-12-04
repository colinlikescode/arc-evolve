HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE STAMPING WITH COLOR-ALIGNED MARKERS  ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the TEMPLATE: a small multi-colored pattern (not solid blocks)
• The template has ANCHOR COLORS at specific positions (corners, edges, center)
• Find MARKERS: isolated cells or solid rectangular blocks of non-background colors
• Each marker's color matches one of the anchor colors in the template

FOR EACH MARKER:
1. Identify which position in the template has the marker's color
2. Scale the template to match the marker's size (1x1 marker = 1x scale, 2x2 = 2x scale, etc.)
3. Place the scaled template so the anchor position aligns WITH the marker location
4. The connection/fill between nearby markers uses the template's "body" color

KEY INSIGHT:
• Marker color determines ALIGNMENT (which template corner/position goes there)
• Marker size determines SCALE of the template copy
• The original template and markers remain; additional template structure is added
"""
