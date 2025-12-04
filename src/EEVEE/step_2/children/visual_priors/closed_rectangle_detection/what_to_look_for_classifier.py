CLASSIFIER_PROMPT = """Does this puzzle involve DISTINGUISHING CLOSED RECTANGLES FROM INCOMPLETE SHAPES?

Look for these indicators:
- The input contains multiple shapes made of a single non-background color
- Some shapes form COMPLETE closed rectangles (all four sides connected, forming a hollow or solid rectangular boundary)
- Other shapes are INCOMPLETE - they have gaps, missing sides, or are just fragments (L-shapes, lines, partial borders)
- In the output, the COMPLETE closed rectangles are recolored to a different color
- The INCOMPLETE shapes remain unchanged in their original color

Key observations:
- Are there rectangular outlines that are fully connected vs. partial/broken shapes?
- Do complete rectangles get transformed while fragments stay the same?
- Is the transformation about identifying "wholeness" or "completeness" of rectangular forms?

Answer ONLY with: YES or NO"""
