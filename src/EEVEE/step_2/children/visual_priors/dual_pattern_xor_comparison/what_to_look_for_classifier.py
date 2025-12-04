CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING TWO PATTERN REGIONS to find differences?

Look for these indicators:
- The input grid appears to be divided into two equal-sized regions (top/bottom or left/right halves)
- Each region contains a different non-zero color forming a pattern
- The output grid is the same size as ONE of these regions (half the input)
- The output marks specific positions with a new color not present in the input

The transformation finds where the two patterns DIFFER:
- Cells where one region has a non-zero value and the other has background
- This is similar to an XOR operation between the two pattern masks

Look at the training examples:
- Is the input split into two halves with different colored patterns?
- Is the output half the size of the input?
- Does the output highlight positions where only ONE of the two patterns has a colored cell?

Answer ONLY with: YES or NO"""
