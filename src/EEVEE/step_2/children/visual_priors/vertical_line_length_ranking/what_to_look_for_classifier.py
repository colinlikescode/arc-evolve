CLASSIFIER_PROMPT = """Does this puzzle involve RANKING VERTICAL LINES BY LENGTH?

This pattern means:
- The input contains multiple vertical lines/columns of a single marker color
- Each vertical line starts at a different row (varying lengths from start to bottom of grid)
- The transformation assigns different colors to each vertical line
- Colors are assigned based on the LENGTH RANK of each line
- The longest line gets one color, second longest gets another color, etc.

Look at the training examples:
- Are there vertical columns of a single non-background color at different column positions?
- Do these columns start at different rows (creating different lengths)?
- In the output, is each column replaced with a different color?
- Does the color assignment correlate with how long each vertical line is?

Answer ONLY with: YES or NO"""
