CLASSIFIER_PROMPT = """Does this puzzle exhibit a HEADER ROW EXPANSION pattern?

This pattern means:
- The input has a "header" row at the top containing distinct colored cells (a sequence of different values)
- Below the header is a "separator" row filled with a uniform color
- The rest of the grid below the separator is empty (filled with zeros/background)
- The output keeps the header and separator intact
- The empty region below is filled by repeatedly cycling through the header colors, where each color becomes a full horizontal row (all cells in that row have the same color)

Look at the training examples:
- Is there a top row with multiple distinct non-zero values?
- Is the second row filled with a single uniform non-zero value (acting as a separator)?
- Are all remaining rows in the input filled with zeros?
- In the output, does each header color expand into a full horizontal row?
- Do the expanded rows cycle through the header colors repeatedly to fill the empty space?

Answer ONLY with: YES or NO"""
