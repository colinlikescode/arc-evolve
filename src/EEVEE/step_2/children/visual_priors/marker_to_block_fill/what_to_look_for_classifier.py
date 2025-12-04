CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-TO-BLOCK EXPANSION in a grid divided into regions?

Marker-to-block expansion means:
- The input grid can be conceptually divided into equal-sized regions (e.g., 3x3 blocks in a 9x9 grid)
- Sparse marker cells (non-zero, non-background) appear scattered in the input
- Each marker indicates that its ENTIRE containing region should be filled with a single fill color
- The output replaces each region containing a marker with a solid block of the fill color
- Regions without markers remain as background

Look at the training examples:
- Is the grid divisible into equal rectangular regions?
- Are there isolated marker cells (single non-zero cells) in the input?
- Does each marker cell cause its entire containing region/block to become filled?
- Do regions without markers stay as background in the output?

Answer ONLY with: YES or NO"""
