HINT = """
╔══════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: THIS IS AN L-SHAPED EXTENSION PUZZLE          ║
╚══════════════════════════════════════════════════════════════╝

THE TRANSFORMATION RULE:
• Each non-zero cell in the input creates an L-shaped extension
• The L-shape consists of two parts:
  1. HORIZONTAL: Extend the cell's color rightward to the right edge of the grid
  2. VERTICAL: From the rightmost column, extend downward to the bottom of the grid

VISUAL PATTERN:
```
Input:           Output:
. . X . .        . . X X X
. . . . .   →    . . . . X
. . . . .        . . . . X
```

KEY OBSERVATIONS:
• The original cell position is preserved
• Horizontal extension: same row, from cell column to last column
• Vertical extension: last column, from cell row+1 to last row
• Multiple colored cells each create their own independent L-shape
• L-shapes may overlap at the right edge column
"""
