HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  FRAME EXTRACTION WITH PATTERN EXPANSION                 ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:

1. FIND THE FRAME: Locate 4 corner markers (same color) forming a rectangle
   - The corners define the output dimensions
   - Two different colors form the left and right vertical sides

2. FIND THE PATTERN: Locate a small shape elsewhere made of the same two side colors
   - This pattern contains the "template" for filling

3. BUILD THE OUTPUT:
   - Output size = frame height × frame width (including corners)
   - Place corner markers at all 4 corners
   - For each side color: expand its portion of the small pattern vertically
     to fill the frame height (between corners)
   - The left half gets one color's expanded pattern
   - The right half gets the other color's expanded pattern

KEY INSIGHT: The small pattern shows the horizontal structure, and the frame's
height determines how many rows to replicate/extend each color's pattern.
"""
