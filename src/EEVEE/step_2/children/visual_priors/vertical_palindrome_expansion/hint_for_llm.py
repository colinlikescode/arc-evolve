HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: VERTICAL PALINDROME / REFLECTION EXPANSION    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The output has the SAME WIDTH as the input
• The output HEIGHT is determined by creating a vertically symmetric pattern

HOW IT WORKS:
• Take the input rows as a "unit"
• The output repeats this unit pattern with vertical reflection
• Think of it as: input rows + reversed middle rows + input rows...
• The pattern creates vertical palindrome segments

CONCEPTUAL STRUCTURE:
If input has rows [A, B, C, D]:
Output follows pattern like: [A, B, C, D, C, B, A, B, C, D, C, B, A...]
Or equivalently: the input block is reflected, creating a wave-like vertical repetition

KEY INSIGHT:
• First row and last row act as "turning points" in the reflection
• Middle rows get mirrored between these anchor rows
• The output height = (2 × input_height - 2) × N + 1, where N depends on creating a square-ish or specific aspect ratio
"""
