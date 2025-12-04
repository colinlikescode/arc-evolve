CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING HOLLOW RECTANGLES TO FIND THE FILLED ONE?

Look for these indicators:
- The input contains multiple distinct rectangular shapes made of a single non-background color each
- Each rectangle has a border/outline made of one color
- The rectangles have hollow interiors (filled with background color)
- One rectangle is "complete" or "fully filled" (no gaps in its border) while others have incomplete borders or missing sections
- The output is a small grid filled with a single color

Check the training examples:
- Are there two or more rectangular outlines in the input?
- Do the rectangles have different interior sizes (the hollow part)?
- Does the output color match the color of the rectangle with the SMALLER interior (more "filled")?
- Is the output a small solid rectangle of that color?

Answer ONLY with: YES or NO"""
