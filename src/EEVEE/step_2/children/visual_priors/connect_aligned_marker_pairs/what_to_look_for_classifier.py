CLASSIFIER_PROMPT = """Does this puzzle involve CONNECTING ALIGNED MARKER PAIRS WITH LINES?

Look for these indicators:
- The input contains scattered marker cells (a single non-background color) on a background
- Markers appear to form pairs that are aligned either horizontally (same row) or vertically (same column)
- In the output, pairs of markers that share the same row or column are connected by a line of a different fill color
- The markers themselves remain unchanged; only the cells BETWEEN aligned pairs are filled
- Unpaired markers (those with no partner in the same row or column) remain isolated with no connecting line

Check the training examples:
- Are there isolated non-background cells in the input?
- Do aligned pairs get connected by a line in the output?
- Is a secondary color used to fill the gap between aligned markers?

Answer ONLY with: YES or NO"""
