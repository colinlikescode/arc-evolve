CLASSIFIER_PROMPT = """Does this puzzle exhibit FRAME EXPANSION WITH COLOR INVERSION?

Frame expansion with color inversion means:
- The input contains a rectangular pattern with two distinct non-background colors
- One color forms an outer frame/border around the other
- The inner region contains a different color (the "core" color)
- The output shows the same pattern expanded outward
- The expansion creates new outer layers where the two colors swap their frame/fill roles
- The growth amount corresponds to the dimensions of the inner region

Look at the training examples:
- Is there a bordered rectangular shape with two non-background colors?
- Does one color form a frame around the other?
- Does the output show the pattern grown larger with an additional outer ring?
- Do the colors appear to swap roles in the expansion (inner becomes outer frame, outer fills new inner areas)?

Answer ONLY with: YES or NO"""
