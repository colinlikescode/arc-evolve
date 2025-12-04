CLASSIFIER_PROMPT = """Does this puzzle involve COMPARING RECTANGULAR FRAMES and FILLING HOLES based on a REFERENCE FRAME?

Look for these indicators:
- Multiple rectangular frames/boxes made of a non-background color scattered in the grid
- Each frame has a border made of one color and may contain holes (background-colored cells) inside
- One or more frames appear to be "complete" or "solid" (filled entirely with the frame color inside)
- Other frames have holes/gaps inside their borders
- The transformation fills holes in some frames with a marker color while leaving other frames unchanged

Key pattern:
- Frames that are completely filled (no holes inside) serve as the REFERENCE
- Frames with holes inside get those holes filled with a different marker color
- The frame with the LARGEST interior hole area remains unchanged (it's the reference)

Answer ONLY with: YES or NO"""
