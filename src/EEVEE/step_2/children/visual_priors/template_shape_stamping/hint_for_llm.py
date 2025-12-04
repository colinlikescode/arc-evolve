HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A TEMPLATE STAMPING PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• One color in the input defines a "template shape" (typically the most prominent connected pattern)
• All OTHER non-background colored cells are "stamp positions"
• Output size = input_height × template_height, input_width × template_width

FOR EACH non-template colored cell at position (r, c):
• Draw the template shape in the output
• Use that cell's color (not the template color)
• Position it at the scaled location: block starting at (r × template_height, c × template_width)

KEY INSIGHT:
• The template color itself does NOT appear in the output
• It only serves to define the shape that gets replicated
• Each other color "inherits" this shape and gets placed at its corresponding scaled position
"""
