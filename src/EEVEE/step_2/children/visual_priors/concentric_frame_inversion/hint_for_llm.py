HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CONCENTRIC FRAME INVERSION PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input consists of NESTED RECTANGULAR FRAMES (concentric rings)
• Each frame is a 1-cell thick border of a single color
• The transformation REVERSES the layer order (inside-out flip)

CONCEPTUALLY:
• Layer 0 (outermost) → becomes the innermost layer
• Layer 1 (second from outside) → becomes second from inside
• Layer N (innermost) → becomes the outermost layer
• All layers swap positions symmetrically around the center

HOW TO IDENTIFY LAYERS:
• The outermost layer is the border of the grid
• Each subsequent layer is one cell inward
• Continue until reaching the center

YOUR APPROACH:
1. Identify all concentric frame layers and their colors (outside to inside)
2. Reverse the order of colors
3. Rebuild the grid with the reversed color sequence for each layer depth
"""
