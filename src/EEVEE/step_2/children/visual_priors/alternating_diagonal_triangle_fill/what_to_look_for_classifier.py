CLASSIFIER_PROMPT = """Does this puzzle exhibit ALTERNATING TRIANGULAR REGION FILLING along diagonal stripes?

Look for these indicators:
- The input contains a repeating diagonal pattern made of a single non-background color
- The diagonal creates triangular regions (above and below the diagonal line)
- The grid can be viewed as repeating "tiles" or segments separated by the diagonal pattern
- In the output, certain triangular regions are filled with a NEW color not present in the input
- The filling follows an alternating/periodic pattern (not all triangular regions are filled)
- The diagonal marker positions remain unchanged; only background cells in specific regions change

Check if:
- There's a consistent diagonal stripe pattern across the grid
- A new color appears in the output filling specific triangular areas
- The filling alternates in a regular pattern across the horizontal extent

Answer ONLY with: YES or NO"""
