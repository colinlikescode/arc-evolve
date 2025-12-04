CLASSIFIER_PROMPT = """Does this puzzle involve finding the MOST FREQUENT COLOR and filling the entire output grid with it?

Look for these indicators:
- The input is a small grid with multiple different colors
- The output is the same size as the input
- The output is filled entirely with a SINGLE color
- That single color appears to be the one that occurred MOST FREQUENTLY in the input grid

Check the training examples:
- Count how many times each color appears in each input
- Does the output consist entirely of whichever color had the highest count?
- Is the output a uniform/solid grid of one color?

Answer ONLY with: YES or NO"""
