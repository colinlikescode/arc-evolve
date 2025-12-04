CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL STRIPE TILING?

Diagonal stripe tiling means:
- The input contains non-zero values arranged along one or more diagonal lines
- These diagonals contain a repeating sequence of distinct colors
- The output fills the entire grid with a diagonal stripe pattern
- The stripe pattern uses the same colors found in the input diagonals
- Each diagonal line in the output contains a single repeating color
- Adjacent diagonals cycle through the color sequence

Look at the training examples:
- Are non-zero cells in the input arranged along diagonal lines?
- Does the output show a complete diagonal striping pattern?
- Do the stripes use the same distinct colors from the input?
- Is the output the same size as the input but completely filled?

Answer ONLY with: YES or NO"""
