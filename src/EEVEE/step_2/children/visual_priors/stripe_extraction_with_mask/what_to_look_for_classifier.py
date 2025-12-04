CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING COLORED STRIPES/LINES from a grid with a MASKING REGION?

Look for these indicators:
- The input contains multiple horizontal OR vertical lines/stripes of different solid colors spanning most of the grid
- There is a rectangular region filled with a single "masking" color that occludes parts of some stripes
- The stripes appear on both sides of the masking region (or the masking region is at an edge)
- The output is a compact grid where each row (or column) is a single solid color
- The output contains one row/column for each distinct stripe color found in the input
- The stripes are ordered in the output by their position in the input (top-to-bottom or left-to-right)
- The output dimensions match: number of stripes × the width/height of the masking region

Key pattern: The masking region defines the output size, and the transformation extracts the stripe colors in spatial order, removing the background and masking region.

Answer ONLY with: YES or NO"""
