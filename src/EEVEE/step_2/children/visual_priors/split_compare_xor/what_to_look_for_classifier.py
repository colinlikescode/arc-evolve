CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING TWO HALVES SEPARATED BY A DIVIDER LINE?

Look for these indicators:
- The input grid has a vertical (or horizontal) line of a single distinct color running through it
- This line divides the grid into two roughly equal regions
- Each region contains a pattern made of two colors (a background color and another color)
- The output grid is smaller, matching the size of ONE half (excluding the divider)
- The output appears to mark differences or similarities between the two halves

The transformation compares corresponding cells from each half and produces a result based on whether they match or differ.

Answer ONLY with: YES or NO"""
