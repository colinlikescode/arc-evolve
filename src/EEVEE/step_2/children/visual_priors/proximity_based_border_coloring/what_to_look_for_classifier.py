CLASSIFIER_PROMPT = """Does this puzzle exhibit PROXIMITY-BASED BORDER COLORING?

This pattern involves:
- Two opposing borders (either left/right columns OR top/bottom rows) filled with distinct solid colors
- Marker cells of a third color scattered in the interior region between the borders
- The transformation replaces each marker with the color of whichever border it is CLOSER to

Look at the training examples:
- Are there two parallel lines/borders of different colors on opposite edges?
- Are there scattered marker cells of a distinct color in the interior?
- In the output, do markers change to match the nearest border's color?
- Does the "midpoint" between borders determine which color each marker becomes?

Answer ONLY with: YES or NO"""
