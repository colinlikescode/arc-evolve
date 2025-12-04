CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE STAMPING WITH COLOR-ALIGNED MARKERS?

Look for these indicators:
- There is a small multi-colored "template" shape somewhere in the input (typically 3x3 or similar)
- The template has distinct colors at specific positions (like corners or edges)
- There are isolated single cells OR solid rectangular blocks scattered in the grid
- These markers use colors that appear in specific positions within the template
- In the output, copies of the template appear at/near each marker location
- The template copy is aligned so the matching color position coincides with the marker
- For rectangular block markers, the template appears scaled to match the block size

The key insight: markers act as "anchors" that specify both WHERE to place the template and HOW to align it (by matching the marker color to that color's position in the template).

Answer ONLY with: YES or NO"""
