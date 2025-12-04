CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL PROJECTION FROM A BOUNDED FRAME?

Look for these characteristics:
- There is an L-shaped or rectangular frame/border made of one color that encloses or bounds a region
- Inside or adjacent to the frame, there is a distinct "marker" region of a different non-background color
- The grid has a large empty (background) area opposite to where the frame is located
- In the output, the marker color appears as individual cells extending diagonally outward from the frame's corner(s) into the empty space
- The diagonal extends away from the bounded region, like rays projecting outward

Key indicators:
- A frame structure (L-shape or partial rectangle) dividing the grid
- A colored region inside/near the frame that is different from the frame color
- Empty space on the opposite side of the frame
- Output adds diagonal lines of the inner color extending into the empty region

Answer ONLY with: YES or NO"""
