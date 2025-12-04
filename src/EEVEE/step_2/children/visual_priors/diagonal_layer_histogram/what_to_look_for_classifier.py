CLASSIFIER_PROMPT = """Does this puzzle involve DIAGONAL LAYER EXTRACTION / STAIRCASE HISTOGRAM?

This pattern means:
- The input grid has distinct colored regions arranged in diagonal bands or layers emanating from a corner
- Each color forms a connected region that spans a certain "depth" from the edge
- The output transforms these diagonal layers into vertical columns
- Each column in the output represents one color, with height proportional to how many rows/columns that color spans
- Columns are ordered by layer depth (outermost layer first), creating a staircase pattern
- Empty space above each column is filled with the background color (typically black/zero)

Look at the training examples:
- Are there distinct colored regions arranged diagonally from a corner?
- Does the output have a staircase/histogram appearance with decreasing column heights?
- Is each column in the output a single solid color (plus background above)?
- Does the number of distinct colors match the number of columns?

Answer ONLY with: YES or NO"""
