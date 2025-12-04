HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL MARKED ENCLOSED RECTANGLES               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all rectangular regions bounded by a border color
• Identify which rectangles have a MARKER inside (a single cell of the border color within the interior)
• Fill the interior of MARKED rectangles with a fill color
• Leave UNMARKED rectangles unchanged (interior stays as background)
• The marker cell itself is NOT overwritten - it remains visible

HOW TO IDENTIFY REGIONS:
• Look for closed rectangular frames made of a non-background color
• The interior is the area strictly inside the border
• A marker is a single cell of the border color sitting inside the interior

FILL LOGIC:
• Only fill background cells inside marked rectangles
• Use a consistent fill color (different from both background and border)
• Preserve the border and the marker
"""
