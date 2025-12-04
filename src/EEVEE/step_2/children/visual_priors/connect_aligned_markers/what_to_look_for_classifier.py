CLASSIFIER_PROMPT = """Does this puzzle involve CONNECTING ALIGNED MARKERS WITH LINES?

This pattern means:
- The input contains scattered non-zero marker cells on a background (typically zeros)
- Pairs of markers that share the same row are connected by a horizontal line
- Pairs of markers that share the same column are connected by a vertical line
- The connecting lines fill all cells between the two markers with the marker color
- Isolated markers (not aligned with any other marker) remain unchanged

Look at the training examples:
- Are there sparse non-zero cells scattered across the grid?
- In the output, do you see horizontal or vertical lines connecting pairs of markers?
- Do the lines span exactly from one marker to another (filling the gap between them)?
- Are markers that don't align with others left as single points?

Answer ONLY with: YES or NO"""
