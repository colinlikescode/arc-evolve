CLASSIFIER_PROMPT = """Does this puzzle involve MARKING ISOLATED CELLS of a color?

Look for these indicators:
- The input contains a dominant non-zero color and a background color (zero)
- The output is nearly identical to the input, with only a few cells changed
- The cells that change are those of the dominant color that have NO orthogonal (up/down/left/right) neighbors of the same color
- These isolated cells are marked with a different color in the output
- Connected clusters of the dominant color remain unchanged

Check the training examples:
- Do isolated single cells of the main color get converted to a different color?
- Do cells that are part of connected groups remain unchanged?
- Is the transformation about identifying "lonely" cells with no same-color neighbors?

Answer ONLY with: YES or NO"""
