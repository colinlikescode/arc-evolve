CLASSIFIER_PROMPT = """Does this puzzle involve FRAMING NEARBY CLUSTERS of non-zero cells?

Look for these indicators:
- The input has scattered non-zero cells (markers) on a background
- In the output, groups of non-zero cells that are close to each other (within a few cells) get a rectangular border/frame drawn around them
- The frame uses a different color than the original markers
- Isolated single cells (not near other markers) remain unchanged without a frame
- The original marker cells are preserved inside the frames
- The frame extends around the bounding box of each cluster of nearby markers

Answer ONLY with: YES or NO"""
