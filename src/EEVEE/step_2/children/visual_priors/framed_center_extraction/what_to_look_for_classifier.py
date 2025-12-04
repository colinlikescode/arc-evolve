CLASSIFIER_PROMPT = """Does this puzzle involve finding a FRAMED CENTER CELL pattern?

Look for these indicators:
- The input contains scattered non-zero cells of multiple colors
- There is a 3x3 rectangular frame/border made of one color (8 cells forming a square ring)
- Inside this frame, at the center position, there is a DIFFERENT color
- The output is a single 1x1 cell

The key structure to find:
```
A A A
A B A
A A A
```
Where A forms a frame and B is a different color at the center.

Look at the training examples:
- Is there a 3x3 region where the border cells are all one color?
- Is the center cell of that 3x3 region a different color?
- Is the output a single cell containing that center color?

Answer ONLY with: YES or NO"""
