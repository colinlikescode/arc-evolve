HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE REGION → SHAPE DECORATION                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. The grid has TWO REGIONS:
   - TEMPLATE REGION: Non-black background (e.g., green) with decorated shapes
   - TARGET REGION: Black (0) background with plain shapes

2. TEMPLATES show how to decorate shapes:
   - Example: Blue 4x4 frame with cyan 2x2 center = "cyan gets blue frame"
   - Example: Red 3x3 block with yellow 1x1 center = "red gets yellow center"

3. TARGET shapes are plain versions waiting to be decorated:
   - A cyan 2x2 block in black region → add blue frame around it
   - A red 3x3 block in black region → add yellow center inside it

HOW TO SOLVE:

1. IDENTIFY THE TEMPLATE REGION:
   - Find the area with non-zero background (green, blue, etc.)
   - Extract the decorated shape patterns from this region

2. LEARN THE TEMPLATES:
   - For each decorated shape, identify: outer color, inner color, sizes
   - Map: "If you see color X, decorate it with color Y"

3. FIND TARGET SHAPES in the black region:
   - Locate plain colored blocks that match template components
   - Note their positions and sizes

4. APPLY TEMPLATES:
   - For each target shape, apply the matching decoration
   - Add frames around shapes, or centers inside shapes
   - Preserve the shape's position

5. OUTPUT: Same grid but target shapes are now decorated like templates

KEY INSIGHT: The template region is like a "legend" showing before/after - apply those same transformations to matching shapes in the black region!
"""

