HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NOISE REMOVAL / RECTANGLE CLEANING            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains solid rectangular regions of a non-background color
• Scattered isolated cells of the same color appear as "noise"
• Some rectangles may have irregular edges (extra protruding cells)

YOUR TASK:
• Identify the core rectangular regions (contiguous filled blocks)
• Determine the clean bounding box for each rectangle
• KEEP only the clean rectangular shapes
• REMOVE all isolated/scattered cells that are not part of rectangles
• Clean up any cells that extend beyond the main rectangular body

HOW TO DISTINGUISH:
• Rectangles: Dense, filled regions with consistent width/height
• Noise: Isolated cells, single pixels, or small fragments not part of a solid rectangle

OUTPUT: Same grid size, containing only the cleaned rectangular regions with all noise removed
"""
