CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A FRAMED RECTANGULAR REGION?

Look for these indicators:
- The input contains scattered non-background cells acting as "noise" outside a specific region
- There is a rectangular region bounded by corner markers (one non-background color at the four corners)
- Two vertical lines of a different non-background color connect the top and bottom corners on the left and right sides
- The output is a smaller grid that extracts exactly this bounded/framed region
- The frame markers (corners and vertical edges) are preserved in the output

Key structural pattern:
- Corner color appears at positions forming rectangle corners
- A second color forms continuous vertical lines between top and bottom corners
- Everything outside this frame is discarded

Answer ONLY with: YES or NO"""
