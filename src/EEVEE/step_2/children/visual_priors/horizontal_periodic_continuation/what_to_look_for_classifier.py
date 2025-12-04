CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL PERIODIC TILING/CONTINUATION?

Horizontal periodic tiling means:
- The input contains a repeating pattern unit (tile) that appears partially or completely in the left portion of the grid
- The pattern has a detectable period/cycle width where it repeats horizontally
- The output continues/extends this repeating pattern horizontally to fill the entire grid width
- The top rows may be mostly empty (background color) while the pattern exists in the bottom rows
- The pattern unit repeats with the same period across the full width of the output

Look at the training examples:
- Is there a pattern in the left portion that appears to repeat horizontally?
- Does the output extend this pattern to fill the remaining columns?
- Are the rows with content showing periodic repetition?
- Does the output maintain the same row structure but extend horizontally?

Answer ONLY with: YES or NO"""
