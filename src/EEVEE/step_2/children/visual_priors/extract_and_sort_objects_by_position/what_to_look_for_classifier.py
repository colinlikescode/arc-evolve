CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING AND SORTING COLORED OBJECTS BY POSITION?

Look for these indicators:
- The input contains multiple distinct colored objects (connected components of non-zero cells) scattered across the grid
- Each object is a small cluster of cells with the same color
- The output is a rectangular grid where:
  - Each column represents one distinct color from the input
  - Colors appear to be sorted/ordered by their horizontal position in the input (left-to-right)
  - The number of rows in the output corresponds to the height/size of one of the objects

Key patterns to check:
- Are there several separate colored regions in the input?
- Is the output much smaller than the input?
- Does each column in the output contain a single repeated color?
- Does the column order match the left-to-right arrangement of objects in the input?

Answer ONLY with: YES or NO"""
