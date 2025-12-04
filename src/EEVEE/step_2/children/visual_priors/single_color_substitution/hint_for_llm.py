HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A SINGLE COLOR SUBSTITUTION PUZZLE    ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid size remains unchanged
• Identify the color that exists in the input but NOT in any output
• Identify the color that exists in the output but NOT in any input
• Replace ALL instances of the "input-only" color with the "output-only" color
• All other colors remain exactly where they are

HOW TO FIND THE COLORS:
• Compare the set of unique colors in input vs output
• The disappearing color gets replaced by the appearing color
• This is a simple global find-and-replace operation

YOUR APPROACH:
1. Find which color value disappears from input → output
2. Find which color value appears in output but not input
3. Copy the input grid
4. Replace every cell with the disappearing color with the new color
"""
