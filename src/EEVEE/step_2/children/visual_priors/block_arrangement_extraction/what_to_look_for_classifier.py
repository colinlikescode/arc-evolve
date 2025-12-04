CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A BLOCK PATTERN FROM A COMPOSITE SHAPE?

Look for these indicators:
- The input contains a large composite shape made of one dominant color, arranged as rectangular blocks in a grid-like pattern (e.g., 3x3 blocks)
- Some block positions in this grid pattern are filled, others are empty (forming an irregular shape)
- There are scattered "noise" or "marker" pixels of a different color throughout the input
- The output is a small grid (matching the block arrangement dimensions)
- The output appears to encode which block positions are empty/filled using the marker color

The puzzle extracts structural information about the arrangement of blocks in the main shape.

Answer ONLY with: YES or NO"""
