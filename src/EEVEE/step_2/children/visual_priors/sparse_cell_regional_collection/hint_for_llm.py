HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: SPARSE CELL REGIONAL COLLECTION PUZZLE        ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• The input grid is conceptually divided into a 3x3 arrangement of regions
• Each non-zero cell in the input maps to a position in the 3x3 output
• The output position is determined by which region the cell occupies

HOW TO DETERMINE OUTPUT POSITION:
• Divide input rows into 3 bands (top, middle, bottom) → output row
• Divide input columns into 3 bands (left, center, right) → output column
• Use integer division: output_row = input_row // (input_height // 3)
• Similarly for columns: output_col = input_col // (input_width // 3)

KEY INSIGHT:
• Each scattered non-zero cell "votes" for its region
• The output collects all non-zero values into their corresponding regional positions
• Empty regions in the output remain zero
"""
