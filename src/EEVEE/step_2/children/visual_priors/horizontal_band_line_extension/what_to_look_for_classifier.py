CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL BAND LINE EXTENSION?

This pattern involves:
- The grid is divided into horizontal bands/stripes, where each band contains rows of a single uniform color
- Within each colored band, there are one or more "marker" cells of a different color (often the background/zero color)
- These marker cells indicate column positions where a vertical line should be drawn

Look at the training examples:
- Is the grid composed of distinct horizontal bands of uniform colors?
- Are there isolated single cells of a contrasting color (like 0) scattered within these bands?
- In the output, do these marker cells extend into full vertical lines that span the entire height of their respective band?
- Does each band process its markers independently?

Answer ONLY with: YES or NO"""
