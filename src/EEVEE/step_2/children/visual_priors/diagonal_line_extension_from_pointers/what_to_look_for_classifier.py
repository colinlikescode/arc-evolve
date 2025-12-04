CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL LINE EXTENSION FROM A CENTRAL SHAPE?

Look for these indicators:
- There is a small compact shape (like a 2x2 block) made of non-zero colored cells
- There are one or more isolated non-zero cells positioned diagonally adjacent to or near the main shape
- These isolated cells indicate a DIRECTION for diagonal extension
- The output extends diagonal lines from these isolated "pointer" cells, continuing in the same diagonal direction until reaching the grid boundary

Key pattern elements:
- A central/anchor shape (typically a 2x2 block of colored cells)
- One or more isolated colored cells that act as "direction indicators"
- The isolated cells define which diagonal direction(s) to extend lines
- Lines extend from the pointer cells away from the central shape

Answer ONLY with: YES or NO"""
