HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: CROSS-DIVIDED QUADRANT EXTRACTION             ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input is divided by a CROSS pattern (one full row + one full column of a divider color)
• This cross divides the grid into 4 QUADRANTS
• Find the quadrant that contains a UNIQUE MARKER (a cell different from the background AND divider colors)
• The output is that quadrant EXTRACTED (excluding the divider lines)

HOW TO SOLVE:
1. Identify the divider color (forms a complete row AND complete column)
2. Find where the horizontal and vertical divider lines are
3. This creates 4 quadrant regions
4. Locate which quadrant has a cell with a unique/marker color
5. Extract and output that quadrant (without the divider)

NOTE: The marker cell preserves its position within the extracted quadrant.
"""
