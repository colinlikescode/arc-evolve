HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SHAPE CLASSIFICATION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The output is a single cell containing a category code
• The code depends ONLY on the GEOMETRIC PATTERN formed by non-zero cells
• The actual color value used is IRRELEVANT - only the shape matters

PATTERN RECOGNITION:
• Extract the binary mask: where are non-zero cells located?
• Compare this mask to known shape categories from training examples
• Each unique spatial arrangement has its own output code

KEY INSIGHT:
• Two inputs with the same shape but different colors → same output
• Two inputs with different shapes → different outputs
• You must learn the shape-to-code mapping from training examples

YOUR APPROACH:
1. Convert each input to a binary pattern (0 vs non-zero)
2. Match the test input's binary pattern to training patterns
3. Output the code associated with that pattern shape
"""
