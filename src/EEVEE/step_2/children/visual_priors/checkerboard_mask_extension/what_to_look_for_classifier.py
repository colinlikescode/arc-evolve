CLASSIFIER_PROMPT = """Does this puzzle exhibit CHECKERBOARD PATTERN EXTENSION WITH BORDER REMOVAL?

This pattern type means:
- The input contains a checkerboard-like pattern (alternating colors in a diagonal pattern) in one region
- There is a border/margin region filled with a uniform "mask" color along one or more edges
- The mask color forms an L-shape, rectangular strip, or fills the remaining area outside the pattern
- The output removes the mask entirely and extends the checkerboard pattern to fill the full grid
- The extended pattern continues seamlessly, maintaining the alternating diagonal structure

Look at the training examples:
- Is there a repeating alternating pattern (like a checkerboard) in part of the input?
- Is there a solid-colored region (border/mask) that appears to be hiding or replacing part of the pattern?
- Does the output have the same dimensions as the input but with the mask replaced by the extended pattern?
- Does the pattern in the output maintain consistent alternation across the entire grid?

Answer ONLY with: YES or NO"""
