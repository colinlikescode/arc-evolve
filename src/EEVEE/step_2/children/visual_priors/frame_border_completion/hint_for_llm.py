HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A FRAME/BORDER COMPLETION PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find the bounding box of all non-zero cells in the input
• Identify the four edges: top row, bottom row, leftmost column, rightmost column within this bounding box
• Along each edge line, find the span from the first to last non-zero cell
• Fill any gaps (background cells) BETWEEN non-zero cells on these edges with a secondary color
• Keep all original non-zero cells unchanged
• Interior cells (not on the edges) remain as background

KEY INSIGHT:
• Only cells along the perimeter edges get filled
• The fill color is different from the original non-zero color
• Gaps are filled only BETWEEN existing non-zero cells on each edge (not beyond them)
• This "completes" a rectangular frame by connecting sparse border cells
"""
