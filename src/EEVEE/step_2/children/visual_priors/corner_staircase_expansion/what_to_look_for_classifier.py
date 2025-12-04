CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER MARKER STAIRCASE EXPANSION?

Corner marker staircase expansion means:
- The input is mostly empty (background color) with 2-4 colored markers placed at or near corners
- Each corner marker spawns a triangular/staircase pattern growing toward the grid center
- The pattern alternates: a row with colored cells, then a row with background, then a longer row with colored cells
- Each successive filled row extends further into the grid (staircase growth)
- Different corner markers create different colored regions that meet in the middle

Look at the training examples:
- Are there colored markers at corners of an otherwise empty grid?
- Does the output show triangular/staircase patterns emanating from each corner?
- Do the patterns grow in alternating filled/empty rows with increasing length?
- Do multiple corner colors create distinct regions meeting near the center?

Answer ONLY with: YES or NO"""
