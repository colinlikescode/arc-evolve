CLASSIFIER_PROMPT = """Does this puzzle involve EXTENDING LINES FROM A TEMPLATE SHAPE'S OPENING?

Look for these characteristics:
- There is a distinctive geometric shape made of one non-background color (like a funnel, triangle, or bracket shape)
- There are scattered individual cells of a different non-background color (marker cells)
- The geometric shape has an opening or gap at one edge (typically the bottom)
- In the output, vertical lines of the marker color extend from the gap positions in the shape, continuing to the edge of the grid

Key indicators:
- Two distinct non-background colors: one forms a connected shape, the other appears as scattered single cells
- The shape has internal structure with gaps/holes
- Output shows new vertical lines that weren't in the input, drawn in the marker color
- These lines originate from within the shape and extend outward

Answer ONLY with: YES or NO"""
