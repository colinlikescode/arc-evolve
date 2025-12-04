CLASSIFIER_PROMPT = """Does this puzzle involve HIGHLIGHTING INTERIOR CELLS WITHIN MARKED REGIONS?

Look for these indicators:
- The grid has a background color (often black/zero) and a dominant non-background color
- There is a distinct "marker" color that appears in small clustered regions scattered across the grid
- The marker color forms irregular shapes mixed with the dominant color
- In the output, a NEW color (not present in input) appears
- This new color replaces instances of the dominant color that appear WITHIN the bounding area of marker clusters
- The marker color cells themselves remain unchanged
- Cells outside the marker regions remain unchanged

The transformation essentially "fills in" or highlights the dominant-colored cells that are trapped inside or adjacent to marker-color patterns.

Answer ONLY with: YES or NO"""
