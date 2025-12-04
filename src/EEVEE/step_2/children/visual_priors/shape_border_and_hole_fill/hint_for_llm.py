HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SHAPE OUTLINING AND HOLE FILLING PUZZLE       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all connected rectangular shapes made of the non-background color
• For each shape, add a 1-cell thick BORDER around its entire bounding box
  - The border uses a consistent "outline color"
• Identify any "holes" inside each shape (background-colored cells enclosed by the shape's boundary)
• Fill those interior holes with a "fill color"

KEY CONCEPTS:
• "Hollow" shapes = frames with background inside → interior gets filled
• "Solid" shapes = completely filled → just get the border, no interior change
• The original shape color is PRESERVED
• Two new colors are introduced: one for borders, one for filling holes

YOUR APPROACH:
1. Identify each distinct rectangular shape region
2. Compute bounding box and add border layer around it
3. Detect interior cells (background cells enclosed by the shape)
4. Fill interior cells with the fill color
"""
