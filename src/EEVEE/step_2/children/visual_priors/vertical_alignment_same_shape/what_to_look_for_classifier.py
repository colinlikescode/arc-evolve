CLASSIFIER_PROMPT = """Does this puzzle involve VERTICAL ALIGNMENT OF SAME-SHAPED OBJECTS?

Vertical alignment of same-shaped objects means:
- The input contains multiple distinct colored rectangular objects (blocks)
- All objects have the same shape/dimensions
- Objects are scattered at different vertical (row) positions
- In the output, all objects are moved to share the SAME row positions
- Each object keeps its original horizontal (column) position
- The objects become vertically aligned in a single horizontal band

Look at the training examples:
- Are there multiple colored rectangular blocks of identical dimensions?
- Are they scattered vertically in the input?
- In the output, do all blocks occupy the same rows while keeping their column positions?
- Does the output show all objects lined up horizontally?

Answer ONLY with: YES or NO"""
