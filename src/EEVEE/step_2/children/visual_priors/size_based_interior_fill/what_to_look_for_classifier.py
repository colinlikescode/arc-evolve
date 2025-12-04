CLASSIFIER_PROMPT = """Does this puzzle involve RECTANGLE INTERIOR FILLING based on SIZE COMPARISON?

Look for these indicators:
- The input contains multiple solid rectangular regions of the same color
- These rectangles are separated by background (zero) cells
- The rectangles have different sizes (different areas)
- In the output, each rectangle keeps its outer border but has its INTERIOR filled with a different color
- The fill color assigned to each rectangle depends on its SIZE relative to other rectangles

Key questions:
- Are there exactly two (or more) solid rectangles of the same color in the input?
- Do these rectangles have different dimensions/areas?
- In the output, do the rectangles maintain their original border color while having different interior fill colors?
- Does the LARGER rectangle get one fill color and the SMALLER rectangle get a different fill color?

Answer ONLY with: YES or NO"""
