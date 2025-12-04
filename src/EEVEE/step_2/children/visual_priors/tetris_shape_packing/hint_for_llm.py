HINT = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  CRITICAL: TETRIS-STYLE SHAPE PACKING                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

THE PATTERN:

1. Extract all colored SHAPES from the input grid
2. Pack them into a COMPACT RECTANGLE with NO GAPS
3. Most shapes can be ROTATED (0°, 90°, 180°, 270°) but NOT reflected
4. **CRITICAL: The TOPMOST shape (highest in the input) must NOT rotate - keep its original orientation**
5. The output is completely filled - every cell has a color

KEY CONCEPTS:

• SHAPE EXTRACTION: Each distinct color forms one shape
  - Get the relative positions of all cells of each color
  - Normalize so the shape starts at (0,0)

• ROTATION: Shapes can be rotated to fit
  - 90° rotation: (row, col) → (col, -row), then normalize
  - Try all 4 rotations for each shape

• PACKING: Find the arrangement where all shapes fit perfectly
  - Output dimensions can be determined from training examples
  - Total cells in output = sum of all shape sizes
  - Use backtracking search to find valid placement

APPROACH:
1. Extract each shape by color from input
2. Identify which shape is TOPMOST (smallest min row) - this shape CANNOT rotate
3. Determine output grid size from training examples
4. For each shape EXCEPT the topmost, generate all 4 rotations
5. Use backtracking to try placing shapes:
   - Place topmost shape FIRST in its original orientation
   - Place other shapes, trying all rotations and positions
   - Backtrack if no valid placement found
6. Solution is found when grid is completely filled

The shapes are designed to fit together like puzzle pieces - there should be exactly ONE valid packing!
"""

