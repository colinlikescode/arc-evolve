CLASSIFIER_PROMPT = """Does this puzzle exhibit ROW-BASED COLOR PROPAGATION FROM A KEY COLUMN?

This pattern means:
- There is a column (usually the first or leftmost non-background column) containing different colored values that act as "row keys"
- The grid contains regions filled with a specific "placeholder" color (often a single consistent non-background color appearing in blocks/regions)
- In the output, each placeholder cell is replaced with the key color from that same row

Look at the training examples:
- Is there a column with varying colors that seems to define what color each row should use?
- Are there regions filled with a uniform placeholder color (not the background)?
- In the output, do those placeholder regions get "painted" with the row's key color?
- Does the background (typically zero) remain unchanged?

Answer ONLY with: YES or NO"""
