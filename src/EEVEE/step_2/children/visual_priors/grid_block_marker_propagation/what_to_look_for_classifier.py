CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID BLOCK PATTERN COMPLETION WITH MARKER PROPAGATION?

This pattern type has these characteristics:
- The grid is divided into rectangular blocks/tiles by separator lines (rows/columns of a single color, typically zeros)
- Each block has the same dimensions
- Some blocks contain "marker" cells - special non-background colors that appear in certain positions
- These markers appear in some blocks but not others, creating an incomplete pattern
- The transformation propagates/copies markers to corresponding positions in other blocks based on alignment

Look at the training examples:
- Is the grid divided into equal-sized blocks by separator rows/columns?
- Do some blocks contain special colored cells (markers) that differ from the base pattern?
- Do markers in one block appear at the same relative position as markers in horizontally or vertically aligned blocks?
- Does the output complete the pattern by copying markers to aligned blocks that were missing them?

Answer ONLY with: YES or NO"""
