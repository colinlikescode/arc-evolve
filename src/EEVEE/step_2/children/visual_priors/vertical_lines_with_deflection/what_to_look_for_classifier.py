CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL LINES WITH DEFLECTION FROM MARKERS?

This pattern means:
- The input has a row (typically the bottom) containing marker cells at specific column positions
- The input also has scattered "special" cells elsewhere in the grid (different from the markers)
- The output draws vertical lines extending from each marker position
- When a vertical line reaches a row containing a special cell in its "zone", the line deflects (shifts one column toward that special cell from that row onward)

Look at the training examples:
- Is there a row with multiple marker cells that appears to define column positions?
- Are there isolated special cells scattered in the main grid area?
- Does the output show vertical lines that sometimes bend or shift at certain rows?
- Do the bends/shifts correspond to where special cells appear?

Answer ONLY with: YES or NO"""
