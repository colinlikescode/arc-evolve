CLASSIFIER_PROMPT = """Does this puzzle involve GRID REGION COMPRESSION / BLOCK SUMMARIZATION?

This pattern means:
- The input contains a large grid with distinct rectangular regions of uniform color
- These colored regions are arranged in a grid-like layout (like a mosaic or tiled floor)
- The regions are separated from each other and surrounded by a background color (typically zeros)
- Each uniform rectangular region gets compressed to a SINGLE CELL in the output
- The output is a small grid where each cell represents one region from the input
- The spatial arrangement of regions in the input is preserved in the output

Look at the training examples:
- Is there a large grid with multiple solid-colored rectangular blocks?
- Are these blocks arranged in a grid pattern (rows and columns of blocks)?
- Is the output much smaller than the input?
- Does each cell in the output correspond to one block from the input?
- Is the relative position of colors in the output the same as the block positions in the input?

Answer ONLY with: YES or NO"""
