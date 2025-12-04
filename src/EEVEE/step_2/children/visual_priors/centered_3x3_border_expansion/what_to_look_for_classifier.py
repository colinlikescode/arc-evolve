CLASSIFIER_PROMPT = """Does this puzzle exhibit CENTERED 3x3 BORDER EXPANSION around isolated non-zero cells?

This pattern means:
- The input contains one or more isolated non-zero cells scattered on a background
- Each non-zero cell in the output is surrounded by a 3x3 border (the original cell becomes the center)
- The border color is DIFFERENT for each unique center cell value - each distinct non-zero value gets its own unique border color
- The center cell retains its original color value
- The 3x3 bordered region is centered on the original cell position

Look at the training examples:
- Are there isolated single non-zero cells in the input?
- In the output, does each cell become the center of a 3x3 region?
- Is the center cell's original value preserved?
- Are the 8 surrounding cells filled with a consistent border color (different from the center)?
- Do different center values get different border colors?

Answer ONLY with: YES or NO"""
