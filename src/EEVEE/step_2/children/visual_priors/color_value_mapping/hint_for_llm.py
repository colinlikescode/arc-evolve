HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A COLOR MAPPING / SUBSTITUTION PUZZLE ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid structure remains IDENTICAL - same size, same positions
• Each unique color in the input maps to a specific different color in the output
• This mapping is CONSISTENT: the same input color always becomes the same output color
• The mapping must be LEARNED from the training examples

HOW TO SOLVE:
1. Build a color mapping dictionary from ALL training examples
2. For each training pair, match input colors to output colors at the same positions
3. Apply the learned mapping to every cell in the test input

KEY INSIGHT:
• The mapping is a simple substitution cipher for colors
• Examine multiple training examples to discover the complete mapping table
• Each input value has exactly one corresponding output value
"""
