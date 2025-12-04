HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A BLOCK SCALING / CELL EXPANSION PUZZLE ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each cell in the input expands into a block in the output
• Block size = input dimensions (H×W block for each cell)
• Output size = (H×H) rows by (W×W) columns
• The value of input[r][c] fills the ENTIRE block at position (r,c)

VISUAL CONCEPT:
```
Input (3×3):        Output (9×9):
A B C               [AAA][BBB][CCC]
D E F       →       [DDD][EEE][FFF]
G H I               [GGG][HHH][III]
```
Where each [XXX] is actually a 3×3 block filled with value X.

KEY INSIGHT:
• This is NOT fractal/self-similar tiling
• Each cell simply SCALES UP to fill a larger uniform block
• ALL cells expand, including zeros/background
• The spatial arrangement is preserved, just magnified
"""
