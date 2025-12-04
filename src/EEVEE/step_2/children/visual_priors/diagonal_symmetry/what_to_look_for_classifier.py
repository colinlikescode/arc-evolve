CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL SYMMETRY or POINT SYMMETRY?

TWO TYPES OF SYMMETRY TO CHECK:

1. DIAGONAL SYMMETRY: grid[row][col] == grid[col][row]
   - The grid mirrors across the main diagonal (top-left to bottom-right)
   - Top-right triangle equals bottom-left triangle when transposed

2. POINT SYMMETRY (180° ROTATION): grid[row][col] == grid[height-1-row][width-1-col]
   - The grid looks the same when rotated 180° around its center
   - Top-left region equals bottom-right region when rotated 180°
   - A rectangular mask (often filled with 8s) hides part of the pattern
   - The output is the content that belongs in the masked region

Look at the training examples:
- Is there a rectangular region filled with a single repeated value (like 8)?
- Does the rest of the grid show symmetry (diagonal OR point)?
- Is the output a small grid that would fill/replace the masked region?

Answer ONLY with: YES or NO"""

