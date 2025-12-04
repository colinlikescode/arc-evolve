HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE STAMPING BY MARKER ALIGNMENT         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the rectangular "template" - a filled region with embedded markers
• Extract the relative positions of markers WITHIN the template
• Scan the grid for clusters of scattered markers that match those relative positions
• When a match is found, STAMP a copy of the template at that location
• The template is positioned so its internal markers align with the scattered markers

KEY OBSERVATIONS:
• The template has TWO colors: a fill color (rectangle) and a marker color (dots inside)
• Scattered markers outside the template use the SAME marker color
• Each cluster of markers that matches the template's marker pattern gets a stamp
• The original template and all isolated markers remain; new filled regions appear

YOUR APPROACH:
1. Identify the template rectangle and its marker positions (relative to template origin)
2. Find all marker cells outside the template
3. For each potential anchor point, check if scattered markers match template's marker pattern
4. If match found, draw the template rectangle at that position
"""
