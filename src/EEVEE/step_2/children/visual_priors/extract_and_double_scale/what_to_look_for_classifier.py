CLASSIFIER_PROMPT = """Does this puzzle exhibit PATTERN EXTRACTION WITH 2× SCALING?

This pattern type means:
- The input grid contains a small pattern of non-zero cells on a zero/background
- The output extracts just the bounding box region containing the pattern
- Each cell in the extracted pattern is scaled up to become a 2×2 block in the output
- The output dimensions are exactly 2× the height and 2× the width of the pattern's bounding box

Look at the training examples:
- Is there a small pattern of non-zero cells surrounded by background?
- Is the output a scaled-up version of just that pattern (no surrounding background)?
- Does each original cell appear to become a 2×2 block of the same value?
- Is the output size approximately 2× the pattern's bounding box dimensions?

Answer ONLY with: YES or NO"""
