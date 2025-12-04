HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: RECTANGULAR BORDER DECORATION PATTERN         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find each solid rectangular region of non-background color in the input
• Replace each rectangle with a 3-layer "picture frame" pattern:
  - CORNERS: The 4 corner cells get one specific color
  - EDGES: All border cells that are NOT corners get a second color
  - INTERIOR: All cells inside the border get a third color

VISUAL STRUCTURE:
```
C E E E C      C = corner color
E I I I E      E = edge color  
E I I I E      I = interior color
C E E E C
```

KEY OBSERVATIONS:
• The original shape/position of each rectangle is preserved
• Background cells remain unchanged
• The same 3-color scheme is applied consistently to ALL rectangles
• For very small rectangles, some layers may be absent (e.g., no interior if too small)

YOUR CODE MUST:
1. Identify all connected rectangular regions of non-background color
2. For each rectangle, determine its bounding box
3. Apply the corner/edge/interior color mapping based on position within the rectangle
"""
