CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL STREAK/TRAIL EXPANSION?

Diagonal streak expansion means:
- The input is a single row (1×N grid)
- The output is a square grid where the input pattern appears as diagonal streaks
- The non-zero elements from the input form diagonal lines that travel from top-right toward bottom-left
- Each non-zero element creates its own diagonal trail
- The output size is determined by the positions of non-zero elements in the input

Look at the training examples:
- Is the input a single row?
- Does the output show diagonal lines moving from upper-right to lower-left?
- Do the non-zero values from the input appear repeatedly along diagonal paths?
- Does the first non-zero element (from the left) determine when the full pattern starts appearing?
- Is the output square, with dimensions related to the input width and position of non-zero elements?

Answer ONLY with: YES or NO"""
