CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE EXTRACTION WITH MARKER OVERLAY?

This pattern involves:
- Multiple rectangular frames/boxes outlined by one color (the "frame color") in the input
- One frame is the LARGEST and serves as the template
- Scattered marker cells of a DIFFERENT color appear throughout the grid (inside and outside frames)
- The output extracts the largest frame's shape and size
- The frame color in the output is REPLACED by the marker color
- Marker positions that fall INSIDE the template region are preserved in the output

Look at the training examples:
- Are there rectangular bordered regions drawn with one consistent color?
- Is there a secondary color appearing as scattered individual cells?
- Does the output have the same dimensions as the largest rectangular frame?
- Is the output's border/frame drawn in the scattered marker color (not the original frame color)?
- Are interior marker positions from the template preserved?

Answer ONLY with: YES or NO"""
