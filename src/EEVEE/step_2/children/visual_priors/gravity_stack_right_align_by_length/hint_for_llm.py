HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: GRAVITY STACK + RIGHT-ALIGN BY LENGTH         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The bottom row is an ANCHOR/FLOOR - it stays fixed
• All other horizontal segments (contiguous non-zero cells) are collected
• Segments are SORTED BY LENGTH (shortest to longest)
• Segments are RIGHT-ALIGNED and STACKED from bottom up
• Shortest segments appear at the top, longest just above the anchor
• Empty space fills above the stacked segments

CONCEPTUAL PROCESS:
1. Identify the anchor row (full-width row at bottom)
2. Extract all horizontal line segments from the input
3. Sort segments by their length (ascending)
4. Place them right-aligned, stacking from bottom to top
5. Longest segment sits just above anchor, shortest at top of stack
"""
