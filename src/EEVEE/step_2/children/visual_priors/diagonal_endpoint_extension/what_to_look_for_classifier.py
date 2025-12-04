CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL LINE CONTINUATION WITH MARKER PLACEMENT?

Look for these indicators:
- The input contains one or more diagonal line segments made of non-zero cells
- The diagonal segments follow a consistent direction (either top-left to bottom-right, or top-right to bottom-left)
- There may be multiple separate diagonal segments with the same orientation
- The output preserves the original diagonal segments
- New marker cells of a DIFFERENT color appear at positions that would CONTINUE each diagonal line in BOTH directions until blocked or reaching the grid boundary

Key observations:
- Each diagonal segment gets "extended" conceptually in both directions
- The extension markers are placed at the next cell positions along the diagonal trajectory
- The marker color is different from the original diagonal color
- The original diagonal cells remain unchanged

Answer ONLY with: YES or NO"""
