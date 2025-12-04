CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL LINE DRAWING BETWEEN SAME-ROW MARKER PAIRS?

This pattern involves:
- Scattered marker cells (non-zero, non-background) placed sparsely on a background
- When TWO marker cells appear on the SAME ROW, a connecting line is drawn between them using a secondary color
- When TWO marker cells appear in the SAME COLUMN, a connecting line is drawn between them using the same secondary color
- The original marker cells remain unchanged; only the cells BETWEEN paired markers get filled

Look at the training examples:
- Are there sparse marker cells scattered on a mostly empty background?
- Do pairs of markers that share the same row get connected by a horizontal line?
- Do pairs of markers that share the same column get connected by a vertical line?
- Is a new color (different from both background and marker) used for the connecting lines?
- Do the lines go between the markers but NOT over them?

Answer ONLY with: YES or NO"""
