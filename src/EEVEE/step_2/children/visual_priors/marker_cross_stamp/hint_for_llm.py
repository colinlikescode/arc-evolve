HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A MARKER EXPANSION / STAMP PATTERN    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all marker cells (the non-background, non-zero cells in input)
• Each marker gets replaced with a fixed cross/plus template pattern
• The template is centered on the marker position

THE CROSS TEMPLATE STRUCTURE:
• Center: keeps the marker color
• One cell ABOVE center: first accent color
• One cell BELOW center: second accent color  
• One cell LEFT of center: third accent color
• One cell RIGHT of center: fourth accent color

BOUNDARY HANDLING:
• When the marker is near an edge, only draw the parts of the cross that fit
• The cross is clipped at grid boundaries, not wrapped

YOUR APPROACH:
1. Identify all marker cell positions in the input
2. Determine the cross template colors from training examples
3. For each marker position, stamp the cross pattern (clipping at boundaries)
4. The background remains unchanged where no cross is placed
"""
