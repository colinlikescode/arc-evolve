CLASSIFIER_PROMPT = """Does this puzzle involve FILLING RECTANGULAR FRAMES BASED ON INTERIOR SIZE?

Look for these indicators:
- The input contains multiple rectangular frames/boxes made of a single border color
- Each frame has an empty interior (filled with background color)
- Some frames may have a single marked cell inside (acting as a "key" or reference)
- The frames have different interior dimensions (e.g., 1x1, 2x2, 3x3, etc.)
- In the output, each frame's interior is filled with a color that depends on the interior size
- Different sized interiors receive different fill colors

The transformation fills each hollow rectangle's interior with a color determined by how large that interior region is.

Answer ONLY with: YES or NO"""
