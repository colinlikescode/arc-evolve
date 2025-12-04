HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: ORIENTED PATTERN ASSEMBLY PUZZLE              ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple small NxN patterns scattered throughout
• Each pattern has a neutral/base color filled with an accent color forming a directional cluster
• The accent color's position within the pattern indicates its ORIENTATION (which corner/edge it points to)
• Extract all distinct patterns and determine each one's directional orientation

ASSEMBLY LOGIC:
• Create an output grid of (N×3) × (N×3) size
• The output is a 3×3 arrangement of the extracted patterns
• Place each pattern in the output position matching its orientation:
  - Pattern pointing top-left → top-left block of output
  - Pattern pointing bottom-right → bottom-right block of output
  - etc.
• The center block is filled with the neutral/base color

YOUR APPROACH:
1. Identify all NxN patterns in the input (look for non-background regions)
2. For each pattern, determine which direction the accent color points
3. Assemble patterns into output grid based on their orientations
"""
