CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL PATTERN REPETITION WITH COLOR REPLACEMENT?

This pattern type means:
- The input grid contains a vertically repeating pattern (a base unit that tiles vertically)
- The input height is a multiple of some base unit height (e.g., 2 repetitions of a 3-row block)
- The output extends this repetition to a different count (e.g., 3 repetitions instead of 2)
- All non-zero cells change to a different non-zero color in the output
- The width stays the same, only the height changes

Look at the training examples:
- Does the input have a vertically repeating structure?
- Is the output taller than the input with the same width?
- Does the output contain more repetitions of the same base pattern?
- Are non-zero values replaced with a different non-zero color?

Answer ONLY with: YES or NO"""
