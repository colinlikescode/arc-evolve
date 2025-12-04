HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: NESTED RECTANGLE COMPRESSION PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains CONCENTRIC RECTANGLES - layers nested inside each other
• Each layer (regardless of its thickness) becomes exactly ONE cell thick in output
• The nesting order is preserved: outermost layer stays outermost, innermost stays innermost

HOW TO SOLVE:
1. Identify all distinct rectangular regions/layers from outside to inside
2. Count the number of layers (including the background)
3. Create an output grid sized to fit all layers with 1-cell thickness each
4. The output dimensions = (2 × number_of_layers - 1) × (2 × number_of_layers - 1)
5. Draw each layer as a 1-cell-thick frame, working from outside inward
6. The center cell represents the innermost region

STRUCTURE EXAMPLE:
Input layers (thick):     Output (compressed):
[Background]              B B B B B
  [Layer 1]         →     B 1 1 1 B
    [Layer 2]             B 1 2 1 B
      [Center]            B 1 1 1 B
                          B B B B B
"""
