CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING THE MOST DENSELY MARKED RECTANGLE from multiple candidate regions?

Look for these indicators:
- The input contains multiple separate rectangular regions filled with a primary/dominant color
- Each rectangle contains scattered marker cells of a secondary/accent color at various positions
- The rectangles have different sizes and different numbers of marker cells
- One rectangle has MORE marker cells (higher density of accent color) than the others
- The output is a single rectangle that matches one of the input rectangles exactly

Key questions:
- Are there multiple distinct rectangular regions separated by background?
- Do all rectangles share the same primary fill color with accent markers?
- Does the output correspond to extracting one specific rectangle from the input?
- Is the selected rectangle the one with the most accent/marker cells?

Answer ONLY with: YES or NO"""
