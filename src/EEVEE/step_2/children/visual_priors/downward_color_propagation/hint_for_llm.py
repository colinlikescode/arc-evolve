HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DOWNWARD COLOR PROPAGATION PUZZLE   ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Process each column independently from TOP to BOTTOM
• Non-zero cells propagate their color downward to fill zeros below them
• Think of it as "color gravity" - colors fall down and fill empty space

HOW IT WORKS:
• For each column, scan from top to bottom
• When you encounter a non-zero cell, remember that color
• Fill all subsequent zero cells with the most recently seen non-zero color
• If a new non-zero color is encountered, it becomes the new "falling" color

VISUAL CONCEPT:
Column:    Becomes:
  A          A
  0    →     A
  B          B
  0          B

YOUR APPROACH:
1. Iterate through each column
2. Track the "current color" as you scan downward
3. Replace zeros with the current tracked color
4. Update tracked color when encountering new non-zero values
"""
