CLASSIFIER_PROMPT = """Does this puzzle involve BLOCK COMPRESSION / REGION EXTRACTION?

Block compression means:
- The input grid is divided into equal-sized blocks (e.g., a 9x9 grid divided into 3x3 blocks)
- Each block is reduced to a single cell in the output
- The output represents a "summary" of each block, typically showing the dominant/uniform color of that region
- There may be a special "marker" color that appears throughout but is ignored in the output
- Blocks that are mostly background produce background in the output

Look at the training examples:
- Is the input grid divisible into equal square blocks?
- Is the output size equal to the number of blocks in each dimension?
- Does each block contain either a uniform colored region or mostly background?
- Is there a color that appears as scattered single cells (markers) that doesn't appear in the output?

Answer ONLY with: YES or NO"""
