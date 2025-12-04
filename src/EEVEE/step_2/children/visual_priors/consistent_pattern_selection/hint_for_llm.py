HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: FIND THE CONSISTENT PATTERN                   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple small patterns (same size) scattered across the grid
• Each pattern is made of a single non-background color
• Multiple colors appear, each with several pattern instances

YOUR TASK:
• For each color, find ALL instances of its pattern in the grid
• Compare the instances: are they IDENTICAL or do they VARY?
• The OUTPUT is the pattern of the color whose instances are ALL IDENTICAL

HOW TO IDENTIFY:
• Extract each small connected pattern by color
• Group patterns by their color
• For each color, check if all its pattern instances have the exact same shape
• The color with perfectly consistent instances → that's your answer
• Output that pattern (the consistent one) in its original form
"""
