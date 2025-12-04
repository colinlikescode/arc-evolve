CLASSIFIER_PROMPT = """Does this puzzle involve HIGHLIGHTING COMPLETE 2x2 BLOCKS of a specific color?

Look for these indicators:
- The grid contains two main colors: a dominant/background color and a secondary color
- The input has various scattered cells of the secondary color
- In the output, some locations where there was a perfect 2x2 block (all four cells) of the secondary color are replaced with a new highlight/marker color
- The highlight color marks complete 2x2 squares of the secondary color
- Other cells remain unchanged

Check if:
- A third color appears in the output that wasn't in the input
- This new color only appears in 2x2 block formations
- These 2x2 blocks correspond to locations where the secondary color formed complete 2x2 squares in the input

Answer ONLY with: YES or NO"""
