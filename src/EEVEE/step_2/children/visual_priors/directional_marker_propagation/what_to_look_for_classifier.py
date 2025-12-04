CLASSIFIER_PROMPT = """Does this puzzle exhibit DIRECTIONAL PATTERN PROPAGATION WITH MARKERS?

This pattern type means:
- The input contains a main template shape (a small connected pattern of non-zero cells)
- There are single-cell or small markers of different colors positioned in cardinal directions (up, down, left, right) relative to the template
- The markers indicate directions for propagation/replication

Look at the training examples:
- Is there one prominent shape that serves as a "template"?
- Are there isolated single cells or small markers of different colors near the template?
- In the output, does the template pattern get replicated multiple times in specific directions?
- Do the replicated copies use the color of the corresponding directional marker?
- Does propagation continue toward the grid boundary in the marker's direction?

Answer ONLY with: YES or NO"""
