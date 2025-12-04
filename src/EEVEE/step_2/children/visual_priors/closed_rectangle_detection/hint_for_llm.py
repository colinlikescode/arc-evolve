HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CLOSED RECTANGLE DETECTION PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Identify all shapes made of non-background cells
• Distinguish between COMPLETE CLOSED RECTANGLES and INCOMPLETE shapes
• A closed rectangle has all four sides forming a continuous rectangular border
• COMPLETE rectangles → recolor to a secondary color
• INCOMPLETE shapes (fragments, L-shapes, lines) → keep original color

HOW TO IDENTIFY CLOSED RECTANGLES:
• Find connected components of non-background cells
• Check if the component forms a rectangular outline
• The outline must be complete (no gaps in the border)
• Interior may be hollow (background) or filled

YOUR APPROACH:
1. Find all distinct connected regions of the primary color
2. For each region, determine if it forms a complete rectangular border
3. Recolor complete rectangles; leave incomplete shapes unchanged
"""
