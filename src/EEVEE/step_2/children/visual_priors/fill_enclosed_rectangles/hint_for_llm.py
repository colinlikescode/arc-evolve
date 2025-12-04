HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FILL ENCLOSED RECTANGULAR REGIONS             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid has a "border" color that forms lines/walls creating rectangular compartments
• Find all CLOSED rectangular regions (bounded on all 4 sides by the border color)
• Fill the INTERIOR cells of each closed rectangle with a new fill color
• The border cells themselves remain unchanged
• Open or incomplete rectangles are NOT filled

HOW TO IDENTIFY CLOSED RECTANGLES:
• Look for rectangular shapes where the border color forms a complete perimeter
• The interior is the region of background cells fully surrounded by the border
• Check that all four edges of the rectangle are present

YOUR CODE MUST:
1. Identify the border/wall color (non-background color forming lines)
2. Find all closed rectangular regions bounded by this border color
3. For each closed rectangle, fill its interior cells with the fill color
4. Leave border cells and non-enclosed areas unchanged
"""
