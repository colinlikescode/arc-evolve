HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RECTANGLE FRAMING WITH CONNECTION LINES       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all rectangular regions of the primary non-background color
• Each rectangle gets FRAMED with a border color (extends outward by the rectangle's dimensions)
• Rectangles are CONNECTED via straight lines using a connector color
• Connection lines extend from each rectangle toward others (vertically and horizontally)
• The connector lines have the same width/height as the corresponding rectangle dimension

KEY OBSERVATIONS:
• Frame color surrounds each rectangle, matching the rectangle's proportions
• Connector color creates paths between rectangles
• Lines extend from rectangles in cardinal directions until they meet or reach grid edge
• Original rectangles remain unchanged; only additions are made

CONCEPTUAL APPROACH:
1. Identify all rectangular regions of the marker color
2. For each rectangle, add a surrounding frame of the frame color
3. Draw connector lines extending from each rectangle's position
4. Connector line thickness matches the rectangle's width/height in that direction
"""
