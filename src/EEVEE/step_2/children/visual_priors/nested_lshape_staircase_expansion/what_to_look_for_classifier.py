CLASSIFIER_PROMPT = """Does this puzzle exhibit NESTED L-SHAPE EXPANSION / STAIRCASE SCALING?

This pattern involves:
- The input contains nested L-shaped or rectangular regions where each color forms a boundary layer
- Colors are arranged in a "staircase" or nested corner pattern (like concentric rectangles meeting at a corner)
- One color (often zero or the outermost color) represents empty/incomplete regions
- The output is exactly 2x the input size in each dimension
- The output completes/extends the nested staircase pattern, filling the empty regions by continuing the layered structure

Look at the training examples:
- Does the input have a corner-based nested pattern where colors form L-shapes or triangular regions?
- Is the output double the size of the input?
- Does the output appear to extend the nested pattern into previously empty areas?
- Are the color boundaries maintained as horizontal/vertical lines that extend based on their nesting level?

Answer ONLY with: YES or NO"""
