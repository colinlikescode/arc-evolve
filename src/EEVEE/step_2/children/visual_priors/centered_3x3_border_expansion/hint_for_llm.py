HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: 3x3 BORDER EXPANSION AROUND EACH CELL         ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Find all isolated non-zero cells in the input
• Each non-zero cell becomes the CENTER of a 3x3 region in the output
• The 8 surrounding cells are filled with a BORDER COLOR
• The border color is DETERMINED BY the center cell's value
• Each distinct center value maps to a specific border color

KEY INSIGHT - COLOR MAPPING:
• There is a fixed mapping from center cell values to border colors
• This mapping is consistent across all examples
• Look at the training examples to deduce which center values map to which border colors

YOUR CODE MUST:
1. Find all non-zero cells in the input
2. Determine the border color for each cell based on its value
3. For each non-zero cell at (row, col):
   - Keep the center cell's original value
   - Fill the 8 adjacent cells with the corresponding border color
4. Handle grid boundaries appropriately
"""
