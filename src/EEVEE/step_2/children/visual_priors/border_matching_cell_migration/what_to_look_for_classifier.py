CLASSIFIER_PROMPT = """Does this puzzle exhibit BORDER-MATCHING CELL MIGRATION?

Border-matching cell migration means:
- The grid has a rectangular frame with different colored borders on each of the four sides (top, bottom, left, right)
- The corners of the frame are background/zero colored
- Inside the frame, there are scattered colored cells
- Some interior cells have colors that match one of the four border colors
- The transformation moves these interior cells to be adjacent to their matching border

Look at the training examples:
- Is there a distinct colored border on each side of the grid?
- Are the corners of the grid the background color (zero)?
- Are there interior cells whose colors match the border colors?
- In the output, do these matching cells appear adjacent to their corresponding border instead of their original position?
- Do non-border-matching interior cells get removed/cleared?

Answer ONLY with: YES or NO"""
