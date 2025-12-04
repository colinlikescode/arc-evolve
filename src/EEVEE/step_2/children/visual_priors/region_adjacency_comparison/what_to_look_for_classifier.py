CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING ADJACENCY COUNTS for distinct regions?

Look for these indicators:
- The input contains multiple distinct solid-colored rectangular regions (like 2x2 blocks) of the same color
- There are scattered single cells of a different "marker" color throughout the grid
- The output is a single cell (1x1)
- The output value seems to be either the background color or the marker color

The transformation appears to compare how many marker cells are adjacent to each distinct region.

Answer ONLY with: YES or NO"""
