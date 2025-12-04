HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  BOUNDED REGION WITH TEMPLATE-GUIDED EXPANSION          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:

1. FIND THE BOUNDED REGION:
   • Locate 4 corner markers (same distinctive color) forming a rectangle
   • The output grid is this rectangular region (corners inclusive)

2. FIND THE TEMPLATE PATTERN:
   • Look for a small pattern OUTSIDE the bounded region
   • This template shows spatial relationships between colors
   • Template indicates which color should fill gaps between blocks

3. APPLY THE TEMPLATE:
   • The template shows relative positions of colors
   • One color in the template represents a "connector" or "filler"
   • Expand the blocks to fill gaps according to template relationships
   • Where template shows color A adjacent to color B, extend those blocks toward each other

4. PRESERVE:
   • Corner markers stay in their corner positions
   • Original colored blocks remain (may be extended)
   • Add filler color in gaps based on template layout

KEY INSIGHT: The template is a miniature map showing how colors relate spatially - use it to determine what fills the empty space between existing blocks.
"""
