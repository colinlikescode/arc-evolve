HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CONCENTRIC LAYER INVERSION PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input consists of concentric rectangular layers/rings of different colors
• Each layer forms a frame around the inner layers (like nested boxes)
• The output INVERTS the layer order: innermost ↔ outermost

HOW TO THINK ABOUT IT:
• Identify all the distinct concentric layers from outside to inside
• Layer 0 (outermost) → becomes the innermost layer in output
• Layer 1 → becomes second-innermost in output
• Continue until the center layer becomes the outermost border

THE GEOMETRY STAYS THE SAME:
• The width/thickness of each layer is preserved
• Only the colors swap positions (inside-out reversal)
• If input layers are [A, B, C, D] from outside-in, output layers are [D, C, B, A]

YOUR CODE MUST:
1. Identify each concentric layer and its color
2. Record the layer order from outside to inside
3. Reconstruct the grid with the layer order reversed
"""
