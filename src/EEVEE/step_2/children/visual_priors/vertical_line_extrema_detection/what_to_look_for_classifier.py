CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING VERTICAL LINE LENGTHS to identify extremes?

Look for these indicators:
- The input contains multiple vertical columns/lines of a single marker color on a background
- The columns start at different rows (have different lengths/heights)
- The output shows only TWO columns highlighted, with different colors
- One output color marks the LONGEST vertical line
- Another output color marks the SHORTEST vertical line
- All other columns are removed/cleared to background

The transformation identifies and highlights the extreme cases (longest vs shortest) among parallel vertical structures.

Answer ONLY with: YES or NO"""
