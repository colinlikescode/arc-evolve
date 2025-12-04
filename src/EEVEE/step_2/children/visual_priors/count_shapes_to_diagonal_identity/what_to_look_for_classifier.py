CLASSIFIER_PROMPT = """Does this puzzle involve COUNTING DISTINCT SHAPES and generating a DIAGONAL IDENTITY PATTERN?

Look for these indicators:
- The input contains multiple separate/distinct connected regions of non-zero cells scattered across the grid
- These regions may have different shapes and sizes
- The output is a small square grid with non-zero cells ONLY on the main diagonal
- The output size (N×N) corresponds to the NUMBER of distinct shapes/regions found in the input
- The output is essentially an identity matrix pattern using the non-zero color

Check the training examples:
- Are there multiple disconnected clusters of colored cells in the input?
- Is the output a square matrix with colored cells only on the diagonal?
- Does the output dimension match the count of distinct regions in the input?

Answer ONLY with: YES or NO"""
