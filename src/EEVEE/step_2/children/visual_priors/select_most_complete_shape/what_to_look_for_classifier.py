CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING THE MOST COMPLETE/FILLED SHAPE from multiple colored regions?

Look for these indicators:
- The input contains multiple distinct colored regions/shapes (different non-zero colors)
- Each colored region forms a connected or semi-connected shape
- The shapes vary in how "complete" or "filled" they are (some have gaps/holes, others are more solid)
- The output is a cropped/extracted version of ONE of these shapes
- The output appears to be the shape that is most "complete" or has the highest fill density within its bounding box

Key observations:
- Are there 2-4 different colored regions scattered in the input?
- Does the output match exactly one of these regions (same color, same shape)?
- Is the selected region the one that appears most "solid" or "rectangular" compared to others?

Answer ONLY with: YES or NO"""
