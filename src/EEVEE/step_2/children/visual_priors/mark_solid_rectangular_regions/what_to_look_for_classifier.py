CLASSIFIER_PROMPT = """Does this puzzle involve DETECTING AND MARKING SOLID RECTANGULAR REGIONS of a minority color?

Look for these indicators:
- The grid contains two colors: a dominant/background color and a secondary color
- The input and output are the same size
- Most of the grid remains unchanged between input and output
- Certain rectangular regions (like 3x3 blocks) that are completely filled with the secondary/minority color get replaced with a different marker color
- These marked regions are "pure" solid blocks - no mixed colors within them

The transformation finds solid rectangular patches of one color and highlights/marks them with a new color.

Answer ONLY with: YES or NO"""
