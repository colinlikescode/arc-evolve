HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL ALIGNMENT OF SAME-SHAPED OBJECTS     ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple distinct colored rectangular objects
• All objects have IDENTICAL dimensions (same height and width)
• Objects are at different vertical positions but need to be ALIGNED

HOW TO SOLVE:
1. Identify all distinct colored rectangular objects
2. Confirm they all have the same shape/dimensions
3. Find the row range where objects should align (use one object's rows as reference)
4. Move ALL objects vertically to occupy that same row range
5. Keep each object's original column position unchanged

THE RESULT:
• All objects appear in the same horizontal band
• Objects are arranged side-by-side (each at its original column position)
• Background cells fill the rest of the grid

THINK OF IT AS: Collapsing all objects onto the same horizontal level
"""
