CLASSIFIER_PROMPT = """Does this puzzle involve MULTIPLE DISTINCT COLORED SHAPES being PACKED into a COMPACT RECTANGLE?

CRITICAL indicators for this pattern:

1. INPUT has 3 OR MORE different colored shapes:
   - Each color forms a separate shape (like Tetris pieces: L, T, I, etc.)
   - Shapes are SCATTERED across the grid with gaps between them
   - The grid is mostly empty (black/0s) with colored shapes spread out

2. OUTPUT is a SMALL DENSE rectangle:
   - Output is MUCH SMALLER than input (e.g., 3x4 or 4x4)
   - ALL cells in output are filled - NO black/empty cells
   - Contains ALL the same colors from input, packed tightly

3. ROTATION is involved:
   - Shapes may be rotated (90°, 180°, 270°) to fit together
   - Total colored cells is PRESERVED (count is same in input and output)
   - Shapes fit together like puzzle/Tetris pieces with NO gaps

This is NOT:
- Two-region overlay (splitting grid in half)
- Simple extraction or cropping
- Color substitution

Think: "Are scattered puzzle pieces being assembled into a compact block?"

Answer ONLY with: YES or NO"""

