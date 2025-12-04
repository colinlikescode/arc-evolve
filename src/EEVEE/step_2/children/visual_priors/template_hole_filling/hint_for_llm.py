HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE FILLING WITH PATTERN TRANSFER        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid contains rectangular "templates" bounded by a frame color
• Some templates have "holes" (background-colored cells inside the frame)
• Small colored patterns exist outside the templates
• Each pattern outside a template corresponds to filling holes in a specific template

HOW TO SOLVE:
1. Identify all rectangular regions bounded by the frame color
2. For each framed region, find which cells inside are "holes" (background color)
3. Find small colored patterns located outside all framed regions
4. Match each external pattern to a template based on the SHAPE of the holes
5. Copy the external pattern INTO the holes of the matching template
6. Remove/clear the external patterns that were used for filling

KEY INSIGHT:
• The shape of holes inside a template matches the shape of some external pattern
• External patterns act as "fill instructions" for templates with matching hole shapes
• After transfer, external patterns become background color
"""
