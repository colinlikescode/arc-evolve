CLASSIFIER_PROMPT = """Does this puzzle involve STAGGERED VERTICAL BARS WITH BOTTOM RECOLORING?

Look for these indicators:
- The input contains multiple vertical columns/bars of the same non-zero color
- These columns are "staggered" - they start at different row positions but all extend to the bottom
- The columns appear at regular horizontal intervals (e.g., every other column)
- In the output, the lower portions of some or all columns are changed to a different color
- The recoloring appears to mark the "overlap zone" where multiple columns share the same rows

The transformation identifies where columns overlap vertically and recolors the overlapping bottom section.

Answer ONLY with: YES or NO"""
