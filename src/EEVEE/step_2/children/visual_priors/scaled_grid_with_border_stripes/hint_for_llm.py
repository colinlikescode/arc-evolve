HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SCALED EXPANSION WITH BORDER STRIPE PATTERN   ║
╚══════════════════════════════════════════════════════════════╝

THE INPUT STRUCTURE:
• Main region: top-left (N-1)×(N-1) area containing a shape on background
• Right column: defines vertical stripe colors and their row spans
• Bottom row: defines horizontal stripe colors and their column spans  
• Corner cell: defines the bottom-right corner block color

THE TRANSFORMATION RULE:
• Count consecutive cells of each color in the right column and bottom row
• These counts become the SCALE FACTORS for each row/column section
• Expand the main region by scaling each section according to its stripe width
• Append vertical stripes on the right (each stripe width = its row count)
• Append horizontal stripes at the bottom (each stripe width = its column count)
• Fill corner block with the corner cell color
• The colored shape scales proportionally and stays in its relative position
• Draw diagonal lines (using an accent color) in the background corners of the scaled main region - these go from outer corners toward the scaled shape

KEY INSIGHT:
The border stripes define BOTH the stripe widths AND the scale factors for the corresponding rows/columns of the main region.
"""
