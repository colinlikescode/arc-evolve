CLASSIFIER_PROMPT = """Does this puzzle exhibit UNIFORM ROW DETECTION AND MARKING?

This pattern involves:
- The input is a small grid where each row may or may not have all cells containing the same value
- Rows where ALL cells are identical (uniform/homogeneous rows) are treated specially
- The output has the same dimensions as the input
- Rows that were uniform in the input become filled with a marker color in the output
- Rows that were NOT uniform (had mixed values) become filled with the background color (typically black/zero)

Look at the training examples:
- Are there rows in the input where every cell has the same value?
- Do those uniform rows correspond to a specific color (non-background) in the output?
- Do mixed/non-uniform rows become background-colored in the output?
- Is the output essentially a binary classification of each row (uniform vs non-uniform)?

Answer ONLY with: YES or NO"""
