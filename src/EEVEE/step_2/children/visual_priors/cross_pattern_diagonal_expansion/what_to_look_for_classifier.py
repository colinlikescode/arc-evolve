CLASSIFIER_PROMPT = """Does this puzzle exhibit CROSS-PATTERN EXPANSION WITH CENTER PROPAGATION?

This pattern type means:
- The input contains one or more small cross/plus-shaped patterns (a center cell surrounded by 4 cells in cardinal directions)
- Each cross pattern has two distinct non-zero colors: one at the center and one on the arms
- In the output, each cross pattern is EXPANDED by adding the CENTER COLOR at diagonal positions
- The expansion creates a larger diamond/cross shape where:
  - The original cross pattern remains intact
  - The center color appears at diagonal positions extending outward from the center
  - The arm color is extended along the cardinal directions

Look at the training examples:
- Are there small cross/plus patterns with a center cell and 4 adjacent cells?
- Does the output show the same patterns but with additional cells added diagonally?
- Do the diagonal additions use the CENTER color of the original cross?
- Do the arms extend further in cardinal directions using the ARM color?

Answer ONLY with: YES or NO"""
