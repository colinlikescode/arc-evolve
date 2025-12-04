HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-BASED PATTERN SELECTION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains multiple small colored shapes/patterns
• ONE shape contains a special MARKER cell (a unique color appearing only once)
• The marker identifies WHICH pattern to extract as the output

YOUR TASK:
1. Find the unique marker cell (appears exactly once in the grid)
2. Identify which colored pattern/shape contains this marker
3. Extract that pattern's bounding region as the output
4. Replace the marker cell with the surrounding pattern's color

KEY INSIGHT:
• The marker "points to" the correct pattern to output
• The output uses the pattern's own color, NOT the marker color
• The marker position within the pattern is filled with the pattern color
"""
