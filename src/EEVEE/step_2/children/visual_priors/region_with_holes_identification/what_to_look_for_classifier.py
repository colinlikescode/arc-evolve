CLASSIFIER_PROMPT = """Does this puzzle involve IDENTIFYING A REGION WITH INTERNAL HOLES?

This pattern means:
- The input contains multiple distinct colored rectangular regions on a background
- Most regions are completely solid (filled entirely with their color)
- One region has "holes" - background-colored cells inside its bounding rectangle
- The output is a 1x1 cell containing the color of the region with holes

Look at the training examples:
- Are there multiple separate colored regions scattered on the grid?
- Do most regions appear as solid filled rectangles?
- Is there exactly one region that has gaps/holes (background cells) inside its boundary?
- Is the output a single cell containing one color value?

Answer ONLY with: YES or NO"""
