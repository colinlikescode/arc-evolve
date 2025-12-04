CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL DIVIDER MERGING?

Horizontal divider merging means:
- The input grid has a horizontal line of a single uniform color that spans the full width
- This divider line separates the grid into an UPPER region and a LOWER region
- The output removes the divider line and OVERLAYS/MERGES the two regions into one
- The output height equals the height of one region (approximately half the input minus the divider)
- Non-background cells from BOTH regions appear in the output, combined together

Look at the training examples:
- Is there a horizontal line of uniform color (not the background) spanning the full width?
- Does this line divide the grid into two roughly equal halves?
- Is the output approximately half the height of the input?
- Does the output contain colored cells from BOTH the upper and lower regions?

Answer ONLY with: YES or NO"""
