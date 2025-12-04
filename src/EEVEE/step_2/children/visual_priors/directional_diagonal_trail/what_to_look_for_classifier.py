CLASSIFIER_PROMPT = """Does this puzzle exhibit DIRECTIONAL DIAGONAL TRAIL EXTENSION?

This pattern involves:
- A small 2x2 block of non-zero cells in the input containing exactly two distinct non-background colors
- One color appears to be a "direction marker" that indicates which way to extend
- The other color is the "primary/fill" color
- The output shows a diagonal streak/trail of the primary color extending from the original position
- The trail direction (up-left, up-right, down-left, down-right) is determined by the relative position of the marker within the 2x2 block

Look at the training examples:
- Is there a small 2x2 region with two distinct non-background colors?
- Does one color appear only once (the marker) while another appears more times (the primary)?
- Does the output show a diagonal line/trail extending across the grid?
- Does the trail use only the primary color (not the marker color)?

Answer ONLY with: YES or NO"""
