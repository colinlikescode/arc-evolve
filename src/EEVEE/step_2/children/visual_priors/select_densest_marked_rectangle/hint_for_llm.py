HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SELECT RECTANGLE WITH MOST MARKERS            ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Input contains multiple rectangular regions filled with a dominant color
• Each rectangle has scattered accent/marker cells (a secondary color)
• Your task: Find and extract the rectangle with the MOST marker cells

IDENTIFICATION STEPS:
1. Find all distinct rectangular regions (non-background connected components)
2. For each rectangle, count the number of accent/marker cells
3. The rectangle with the HIGHEST count of markers is the answer
4. Extract that rectangle exactly as-is for the output

KEY INSIGHT:
• The "winner" is determined by marker density/count
• Output dimensions match the selected rectangle's dimensions exactly
• Preserve all cell values from the selected rectangle
"""
