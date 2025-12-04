CLASSIFIER_PROMPT = """Does this puzzle exhibit a TWO-COLOR SWAP transformation?

A two-color swap means:
- Two specific colors in the input grid completely exchange positions in the output
- Every cell containing color A in the input becomes color B in the output
- Every cell containing color B in the input becomes color A in the output
- All other colors remain unchanged in their original positions

Look at the training examples:
- Are there exactly two colors that change positions?
- Do those two colors appear to swap with each other (A→B and B→A)?
- Do all other colors stay exactly where they were?
- Is this swap consistent across the entire grid?

Answer ONLY with: YES or NO"""
