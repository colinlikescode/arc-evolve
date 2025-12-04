CLASSIFIER_PROMPT = """Does this puzzle exhibit a GRID VOTING / MAXIMUM MARKER BLOCK SELECTION pattern?

This pattern involves:
- A grid divided into rectangular blocks/cells by separator lines (typically a single consistent color forming a grid structure)
- Each block contains scattered marker cells of a non-background, non-separator color
- The transformation identifies which block has the MOST markers of the non-background color
- That winning block gets completely filled with the marker color
- All other blocks are cleared (set to background color, keeping only the separator lines)

Look at the training examples:
- Is there a grid structure created by horizontal and vertical separator lines?
- Are there scattered colored markers (not the separator color) distributed across different blocks?
- In the output, is exactly ONE block completely filled with a solid color?
- Are all other blocks cleared to the background color?
- Does the filled block correspond to the block that had the most markers in the input?

Answer ONLY with: YES or NO"""
