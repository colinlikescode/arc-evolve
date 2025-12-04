CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER MARKER TO CENTRAL BLOCK MAPPING?

This pattern means:
- There is a small rectangular block (e.g., 2x2) of a uniform "anchor" color somewhere in the grid
- There are exactly 4 isolated single-cell markers scattered around the grid (not the anchor color)
- Two markers are positioned generally in the "top-left quadrant" relative to the anchor block
- Two markers are positioned generally in the "bottom-right quadrant" relative to the anchor block
- The output replaces the anchor block with a 2x2 arrangement of the 4 marker colors
- The marker positions (relative to the anchor) determine their placement in the output block:
  - Top-left-ish marker → top-left of output block
  - Top-right-ish marker → top-right of output block
  - Bottom-left-ish marker → bottom-left of output block
  - Bottom-right-ish marker → bottom-right of output block
- All other cells become background (zero)

Look at the training examples:
- Is there a small solid-colored rectangular block in the input?
- Are there exactly 4 isolated single-cell markers of different colors?
- Does the output show these 4 colors arranged in a 2x2 block at the anchor's location?
- Are all the scattered markers removed in the output?

Answer ONLY with: YES or NO"""
