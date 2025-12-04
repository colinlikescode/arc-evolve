HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A TWO-COLOR SWAP PUZZLE               ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Two specific colors completely exchange their positions
• Where color A appeared in input → color B appears in output
• Where color B appeared in input → color A appears in output
• All other colors remain unchanged

HOW TO IDENTIFY THE TWO COLORS:
• Find colors that appear in different positions between input and output
• These two colors will have swapped all their occurrences
• Typically these may be commonly occurring colors in the grid

YOUR APPROACH MUST:
1. Identify which two colors are being swapped (compare input/output positions)
2. Create output by copying input
3. Replace all occurrences of color A with color B
4. Replace all occurrences of color B with color A
"""
