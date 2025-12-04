HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: MARKER-TO-FILL-COLOR MAPPING PUZZLE           ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into rectangular sections by separator lines
• Each section contains ONE marker cell (non-background, non-separator)
• The marker's color value determines the fill color for that entire section

KEY INSIGHT - COLOR MAPPING:
• There is a fixed offset between marker value and output fill color
• Formula: output_fill_color = marker_value + CONSTANT_OFFSET
• Determine this offset by examining how marker values map to fill colors

YOUR APPROACH MUST:
1. Identify the separator color (forms grid lines dividing sections)
2. Identify the background color (fills most of each section)
3. For each section, find the single marker cell
4. Compute the fill color using: marker_value + offset
5. Fill the entire section with that computed color
6. Preserve all separator lines unchanged

NOTE: The offset is consistent across ALL sections and examples.
"""
