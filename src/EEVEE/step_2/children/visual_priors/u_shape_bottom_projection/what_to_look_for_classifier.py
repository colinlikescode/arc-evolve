CLASSIFIER_PROMPT = """Does this puzzle involve MARKING THE BOTTOM ROW BELOW U-SHAPED PATTERNS?

Look for these characteristics:
- The input contains one or more small "U-shaped" or "bracket" patterns made of non-zero cells
- Each pattern has a structure like: 3 connected cells in a row, with 2 cells directly below on the outer positions (creating a gap/opening in the middle)
- The output preserves all original patterns unchanged
- New marker cells appear on the BOTTOM ROW of the grid
- Each marker is positioned directly below the center/gap of each U-shaped pattern
- All markers use the same distinct color (different from the pattern colors)

Does the transformation add markers at the bottom row aligned with openings in bracket-like shapes?

Answer ONLY with: YES or NO"""
