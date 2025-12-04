HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE REPLACEMENT AT MARKER LOCATIONS      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify the TEMPLATE: a pattern containing multiple distinct non-background colors
• Identify the MARKERS: regions of a single uniform color that match the template's shape
• The marker color is used ONLY in marker regions (not in the template)

OUTPUT CONSTRUCTION:
• For each MARKER region: replace it with a copy of the TEMPLATE pattern
• The original TEMPLATE location: becomes background (zeros)
• Marker positions align with where the template should be placed

KEY INSIGHT:
• The template is the "stamp" - it has the colorful design
• Markers are "placeholders" - same shape, single color
• Copy the template TO each marker location, erase the original template
"""
