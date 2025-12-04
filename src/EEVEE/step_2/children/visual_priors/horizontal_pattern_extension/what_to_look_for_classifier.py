CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL PATTERN EXTENSION/TILING?

Horizontal pattern extension means:
- The input has one or more rows containing a repeating pattern (non-zero cells)
- The remaining rows are filled with the background color (zeros)
- The output keeps the same height but doubles the width
- The patterned rows are extended horizontally by continuing/repeating the pattern
- The background rows remain as background (all zeros) but also doubled in width

Look at the training examples:
- Does the input have horizontal stripe(s) of non-zero values surrounded by zero rows?
- Is the output exactly 2x wider than the input while keeping the same height?
- Are the non-zero pattern rows extended horizontally (continuing the repeating pattern)?
- Do the zero/background rows stay as zeros but doubled in width?

Answer ONLY with: YES or NO"""
