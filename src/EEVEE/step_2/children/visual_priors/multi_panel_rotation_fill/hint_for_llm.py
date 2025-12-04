HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MULTI-PANEL ROTATION/REFLECTION PATTERN       ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into panels by separator columns
• The first panel contains the source pattern
• Empty panels must be filled with transformed versions of the source

TRANSFORMATIONS APPLIED:
• Second panel: Rotate the source pattern 180 degrees
• Third panel: Transpose the source pattern (swap rows and columns)

YOUR APPROACH:
1. Identify the separator column value (appears as a vertical line)
2. Extract the source pattern from the first panel
3. Fill the second panel with the 180° rotation of the source
4. Fill the third panel with the transpose of the source
5. Keep separator columns unchanged

NOTE: The separator columns remain in place - only transform the content panels.
"""
