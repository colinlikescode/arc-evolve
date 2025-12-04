CLASSIFIER_PROMPT = """Does this puzzle involve COMPLETING A RECTANGULAR FRAME/BORDER?

Look for these indicators:
- The input contains non-zero cells that form a sparse rectangular frame or border pattern
- Non-zero cells appear primarily along what would be the edges of a rectangle (top row, bottom row, left column, right column of a bounded region)
- There are gaps (background/zero cells) between non-zero cells along these edge lines
- The output fills in these gaps along the edges with a secondary color, while keeping the original non-zero cells
- The interior of the rectangle remains mostly unchanged (background)

The transformation "completes" or "connects" the perimeter by filling gaps along each edge between existing non-zero cells.

Answer ONLY with: YES or NO"""
