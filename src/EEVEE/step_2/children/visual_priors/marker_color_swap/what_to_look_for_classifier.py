CLASSIFIER_PROMPT = """Does this puzzle exhibit a MARKER-BASED COLOR SWAP pattern?

This pattern involves:
- The input contains exactly TWO distinct colors
- One color acts as a "marker" or "selector" color (often the same special color across examples)
- The other color is the "content" color that varies between examples
- In the output:
  - Positions where the MARKER color appeared → become the CONTENT color
  - Positions where the CONTENT color appeared → become background (zero/black)

Look at the training examples:
- Are there exactly two colors in each input?
- Does one color seem to be a consistent "marker" across examples?
- In the output, do marker positions show the other color, while original content positions become black?

Answer ONLY with: YES or NO"""
