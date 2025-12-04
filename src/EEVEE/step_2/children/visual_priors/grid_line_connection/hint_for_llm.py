HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A GRID LINE CONNECTION PUZZLE         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The grid is divided into cells by separator lines (a consistent divider color)
• Each cell can contain background OR a colored marker

FOR EACH COLOR (excluding background and separator):
• Find all cells in the SAME ROW containing that color
• If 2+ cells exist, fill ALL cells BETWEEN the leftmost and rightmost with that color
• Find all cells in the SAME COLUMN containing that color  
• If 2+ cells exist, fill ALL cells BETWEEN the topmost and bottommost with that color

KEY OBSERVATIONS:
• This creates horizontal and vertical "lines" connecting matching markers
• Connections happen independently for each color
• Separator grid structure is preserved
• Single isolated markers remain unchanged (no pair to connect to)
"""
