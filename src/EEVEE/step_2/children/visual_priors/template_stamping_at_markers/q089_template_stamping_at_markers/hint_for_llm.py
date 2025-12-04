HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A TEMPLATE STAMPING PUZZLE            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input contains one or more TEMPLATE shapes (multi-cell connected patterns)
• The input also contains isolated MARKER cells (single cells of a specific color)
• Each marker color corresponds to a specific template that contains that color

YOUR TASK:
• Identify each template shape and note which "special" color it contains
• Find all isolated single-cell markers in the grid
• For each marker: stamp/copy the corresponding template at that location
• Align the template so the special color cell in the template matches the marker position
• The original templates remain in place; markers get expanded into full templates

KEY INSIGHT:
• A marker color appears BOTH inside a template AND as isolated cells
• The isolated cells are "requests" to place that template there
• Position the template so its marker-colored cell overlaps the marker location
"""
