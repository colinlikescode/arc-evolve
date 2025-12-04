HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A COLOR SUBSTITUTION PUZZLE           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid structure and dimensions remain IDENTICAL
• One specific color from the input is REPLACED with a different color
• All other colors remain UNCHANGED in their positions

HOW TO IDENTIFY THE SUBSTITUTION:
• Compare input and output cell by cell
• Find which color in the input never appears in the output
• Find which color in the output never appears in the input
• These form the substitution pair: old_color → new_color

YOUR APPROACH:
1. Identify the two distinct colors in the input
2. Identify the two distinct colors in the output
3. Find the color that changed (one color is common to both, one differs)
4. Replace every instance of the disappearing color with the new color
5. Keep all other cells unchanged
"""
