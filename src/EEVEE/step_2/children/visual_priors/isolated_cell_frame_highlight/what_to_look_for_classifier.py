CLASSIFIER_PROMPT = """Does this puzzle involve FINDING AN ISOLATED CELL AND FRAMING IT?

Look for these indicators:
- The input has many scattered non-zero cells across the grid
- The output is mostly background (zeros) except for a small 3x3 region
- The 3x3 region has a "frame" pattern: 8 cells of one color surrounding a center cell of a different color
- There appears to be exactly one cell in the input that is completely isolated (all 8 neighboring cells are background/zero)
- The output highlights this isolated cell by creating a 3x3 frame around it

Check the training examples:
- Is there one special cell in each input that has no non-zero neighbors?
- Does the output create a 3x3 bordered region centered on that cell?
- Is the rest of the output filled with background color?

Answer ONLY with: YES or NO"""
