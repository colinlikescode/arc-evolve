CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING THE LARGEST SHAPE from multiple distinct colored shapes?

Look for these indicators:
- The input contains MULTIPLE separate colored regions/shapes (different non-background colors)
- Each shape is spatially distinct (not overlapping)
- The output is a SINGLE extracted shape (one color only, plus background)
- The output appears to be the shape with the MOST non-background cells (largest area)
- The output is cropped to the bounding box of that largest shape

Check the training examples:
- Are there multiple distinct colored objects in each input?
- Is the output always one of those objects extracted?
- Does the selected object appear to have more cells than the others?

Answer ONLY with: YES or NO"""
