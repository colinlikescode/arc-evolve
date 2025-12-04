CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID-DIVIDED BLOCK UNIFORMITY with UNIQUE COLOR SELECTION?

Look for these indicators:
- The grid is divided into rectangular regions by lines of a single "separator" color (forming a grid of blocks)
- Each block in the input contains various colored cells mixed with background (zero) cells
- In the output, each block becomes UNIFORMLY filled with a single non-separator, non-zero color
- The color chosen for each output block appears to be a color that is UNIQUE to that block in the input (appears in that block but not in any other block)
- The separator lines remain unchanged between input and output
- Some blocks may become all zeros if they have no unique color

Look at the training examples:
- Are there horizontal and/or vertical lines of a consistent color dividing the grid into blocks?
- Does each output block contain only one color (plus the separator color)?
- Is the fill color for each block a color that was uniquely present in that input block?

Answer ONLY with: YES or NO"""
