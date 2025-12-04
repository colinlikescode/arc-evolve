CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL-VALUE BASED TILING?

This pattern means:
- The input is a small grid (typically 3x3)
- The output is N times larger in each dimension (e.g., 3x3 → 9x9)
- The output is divided into blocks, each the same size as the input
- The main diagonal of the input contains a consistent "key" color/value
- The input pattern is placed in output blocks corresponding to positions where that diagonal value appears in the input
- All other blocks are filled with zeros/background

Look at the training examples:
- Is the output exactly N times larger than the input in each dimension?
- Do all cells on the main diagonal of the input share the same value?
- Does the input pattern appear in output blocks at positions matching where that diagonal value occurs in the input?
- Are remaining blocks filled with zeros?

Answer ONLY with: YES or NO"""
