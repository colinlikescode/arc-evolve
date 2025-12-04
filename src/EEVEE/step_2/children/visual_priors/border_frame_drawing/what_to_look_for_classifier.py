CLASSIFIER_PROMPT = """Does this puzzle exhibit BORDER FRAME DRAWING?

Border frame drawing means:
- The input is a uniform grid filled entirely with the background color (typically all zeros)
- The output has the same dimensions as the input
- The output has a frame/border drawn around the perimeter using a new color
- The interior cells (all cells not on the edge) remain as the background color
- The first row, last row, first column, and last column are all filled with the frame color

Look at the training examples:
- Is the input a completely uniform grid (all same color)?
- Does the output show a rectangular frame/border around the edges?
- Are the interior cells (not touching any edge) left as the original background color?
- Is the frame exactly 1 cell thick on all sides?

Answer ONLY with: YES or NO"""
