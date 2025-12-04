CLASSIFIER_PROMPT = """Does this puzzle involve FILLING PATTERN CELLS INSIDE A MARKER-BOUNDED REGION?

Look for these indicators:
- The grid has a repeating background pattern using two colors (background and a primary pattern color)
- There is a rectangular region outlined or bounded by a distinct "marker" color (different from both background and primary)
- The marker color forms edges/borders of a rectangular area
- Inside this bounded region, some cells match the primary pattern color while others are the marker color

The transformation would:
- Keep the marker color cells unchanged
- Change the primary pattern color cells INSIDE the marker region to a new fill color
- Leave everything outside the marker region unchanged

Answer ONLY with: YES or NO"""
