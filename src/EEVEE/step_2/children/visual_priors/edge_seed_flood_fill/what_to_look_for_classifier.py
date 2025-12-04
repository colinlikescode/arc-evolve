CLASSIFIER_PROMPT = """Does this puzzle have a color that appears EXACTLY ONCE at COLUMN 0, then FLOOD FILLS to replace all reachable black cells?

Look for these SPECIFIC indicators:

1. INPUT:
   - One specific color appears EXACTLY ONCE in the entire grid
   - That single cell is located at COLUMN 0 (the leftmost column)
   - Other colors appear multiple times scattered around
   - Background is black (0)

2. OUTPUT:
   - The single-occurrence color now fills LARGE AREAS
   - It has spread from column 0 to fill all reachable black cells
   - Other colored cells remain UNCHANGED - they blocked the spread
   - The grid is now mostly filled with the flood color

3. KEY test:
   - Count occurrences of each color in input
   - Is there exactly ONE cell of a certain color?
   - Is that cell at column 0?
   - Does that color dominate the output?

Answer ONLY with: YES or NO"""

