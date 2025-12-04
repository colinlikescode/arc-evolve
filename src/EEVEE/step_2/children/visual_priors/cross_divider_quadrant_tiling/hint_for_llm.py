HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A CROSS-DIVIDER QUADRANT TILING       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into rectangular sections by lines of a single "divider" color
• These divider lines span the full width (horizontal) or full height (vertical)
• Find the section that contains non-background, non-divider colored cells (the "source" pattern)
• Copy this source pattern into ALL other sections at the same relative positions

HOW TO SOLVE:
1. Identify the divider color (forms complete row/column lines)
2. Locate all section boundaries created by these dividers
3. Find which section(s) contain the actual pattern data
4. For each empty section, copy the pattern from the source section
5. Preserve the divider lines in their original positions

KEY INSIGHT: Each section should end up with identical content (excluding dividers)
"""
