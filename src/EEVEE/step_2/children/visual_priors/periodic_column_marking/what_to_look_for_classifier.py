CLASSIFIER_PROMPT = """Does this puzzle exhibit PERIODIC VERTICAL STRIPE MARKING?

This pattern involves:
- A grid with 3 rows containing a repeating pattern of two values (background and dominant color)
- The middle row is typically filled entirely with the dominant color
- The top and bottom rows alternate values in a checkerboard-like pattern
- The transformation marks certain dominant-colored cells with a new "marker" color at regular column intervals

Look at the training examples:
- Is the grid exactly 3 rows tall?
- Does the middle row contain all the same non-background value?
- Do the top and bottom rows show alternating patterns?
- In the output, is a third color introduced at periodic column positions?
- Does the new color appear every N columns (where N matches a repeating unit width)?

Answer ONLY with: YES or NO"""
