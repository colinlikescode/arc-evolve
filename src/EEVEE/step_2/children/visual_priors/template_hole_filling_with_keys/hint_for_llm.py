HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TEMPLATE HOLE FILLING WITH PATTERN KEYS       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains a large rectangular region with a dominant fill color
• This region has "holes" (background-colored cells in specific patterns)
• Small "key" patterns elsewhere show the SAME hole shapes with accent colors
• Keys use the dominant color where the holes have dominant color, and accent colors where holes exist

YOUR APPROACH:
1. Extract the main rectangular region (the large filled area)
2. Identify all hole patterns within it (connected background cells)
3. Find matching key patterns by comparing hole shapes
4. Replace each hole with the corresponding accent colors from its key
5. Output is the filled rectangle with all holes replaced by their key colors

The output is the main region with holes filled according to their matching keys.
"""
