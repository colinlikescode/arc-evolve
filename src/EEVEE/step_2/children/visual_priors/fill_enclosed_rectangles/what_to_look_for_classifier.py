CLASSIFIER_PROMPT = """Does this puzzle involve FILLING ENCLOSED RECTANGULAR REGIONS?

Look for these indicators:
- The grid contains a background color and a "border" or "wall" color that forms lines
- The border color creates rectangular compartments or enclosed regions
- In the output, the INTERIOR of fully-enclosed rectangular regions is filled with a new color
- The border/wall cells themselves remain unchanged
- Only completely closed rectangles get filled (open or incomplete shapes stay empty)

Check the training examples:
- Are there rectangular regions bounded on all four sides by a non-background color?
- Do the interiors of these closed rectangles change to a new fill color in the output?
- Do incomplete or open shapes remain unfilled?

Answer ONLY with: YES or NO"""
