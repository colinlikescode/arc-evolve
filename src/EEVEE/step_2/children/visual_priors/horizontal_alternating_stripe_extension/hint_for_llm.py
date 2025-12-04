HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: HORIZONTAL ALTERNATING STRIPE EXTENSION       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find each isolated non-zero cell in the input
• From that cell's position, extend RIGHTWARD to the grid edge
• Fill with an ALTERNATING pattern: [original_color, separator_color, original_color, separator_color, ...]
• The separator color is consistent across all stripes (look for a color used only in outputs, not inputs)
• The original cell position becomes the first cell of the stripe

KEY OBSERVATIONS:
• Each non-zero input cell triggers its own independent stripe
• Stripes stay on their original row
• The alternation starts with the original color at the original position
• Everything to the LEFT of the original cell remains unchanged (zeros)

YOUR APPROACH:
1. Identify all non-zero cells in the input
2. Determine the separator color (appears in outputs but not as any input cell color)
3. For each non-zero cell at (row, col) with value V:
   - Fill positions from col to the right edge
   - Alternate: V at even offsets, separator at odd offsets from starting position
"""
