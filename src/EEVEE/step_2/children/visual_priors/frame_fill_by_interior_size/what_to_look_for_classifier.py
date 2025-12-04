CLASSIFIER_PROMPT = """Does this puzzle involve FILLING RECTANGULAR FRAMES based on their interior size?

Look for these indicators:
- The input contains multiple closed rectangular frames/borders made of a single non-background color
- Each frame has an empty (background-colored) interior
- The frames have different interior sizes (different width × height of the hollow region)
- In the output, the interior of each frame is filled with a color that depends on the frame's interior area

Key questions:
- Are there multiple hollow rectangular shapes outlined by a consistent border color?
- Do the frames vary in the size of their interior regions?
- In the output, are the interiors filled with different colors based on some property of the frame?

Answer ONLY with: YES or NO"""
