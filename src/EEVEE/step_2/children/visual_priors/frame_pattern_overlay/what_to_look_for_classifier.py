CLASSIFIER_PROMPT = """Does this puzzle involve FRAME-PATTERN OVERLAY/COMPOSITION?

Look for these indicators:
- The input contains TWO distinct non-background structures in different locations
- One structure forms a rectangular FRAME or BORDER (4 line segments forming a rectangle, each side potentially a different color)
- The other structure is a PATTERN made of a single color
- The frame has different colors on its top, bottom, left, and right edges
- The pattern and frame are spatially separated in the input

The transformation combines these by:
- Using the frame as the outer boundary of the output
- Placing the pattern inside the frame
- Extending frame colors inward to fill cells based on the pattern's position

Answer ONLY with: YES or NO"""
