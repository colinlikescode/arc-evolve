HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS A DIAGONAL CASCADE TILING PUZZLE      ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Output dimensions = 2 × input dimensions (height and width)
• The input pattern is placed repeatedly along the main diagonal
• Starting position: top-left corner (0, 0)
• Each subsequent copy shifts by (+1 row, +1 column)
• Continue until the pattern reaches the bottom-right region
• Later placements overwrite earlier ones where they overlap

VISUAL CONCEPT:
```
Input:        Output:
[P]     →     [P . . .]
              [. P . .]
              [. . P .]
              [. . . P]
```
Where P represents the input pattern placed at each diagonal position.

YOUR APPROACH MUST:
1. Create output grid of size (2×input_height, 2×input_width) filled with zeros
2. For each diagonal offset from 0 to input_height-1:
   - Place the entire input pattern at position (offset, offset)
   - When placing, only overwrite with non-zero values OR overwrite all values
3. The result is the input "cascading" diagonally across the output
"""
