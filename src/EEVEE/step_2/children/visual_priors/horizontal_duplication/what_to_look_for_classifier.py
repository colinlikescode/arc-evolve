CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL DUPLICATION/TILING?

Horizontal duplication means:
- The output grid has the SAME HEIGHT as the input
- The output grid has DOUBLE THE WIDTH of the input
- The output consists of the input pattern placed side-by-side with itself (concatenated horizontally)
- The left half of the output is identical to the input
- The right half of the output is also identical to the input

Look at the training examples:
- Is the output exactly twice as wide as the input?
- Is the output the same height as the input?
- Does the output appear to be two copies of the input placed side by side?
- Is there any transformation applied, or is it a direct copy?

Answer ONLY with: YES or NO"""
