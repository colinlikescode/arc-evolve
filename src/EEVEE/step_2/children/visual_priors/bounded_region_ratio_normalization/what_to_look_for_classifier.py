CLASSIFIER_PROMPT = """Does this puzzle involve RATIO NORMALIZATION of a bounded region?

Look for these indicators:
- The input contains a rectangular frame or boundary made of one distinct color (forming an L-shape or U-shape with vertical sides and a bottom)
- Inside this frame, there is a filled rectangular region of a different non-background color
- Above the filled region (within the frame) there may be empty/background cells
- The output is a small fixed-size grid (like 3x3)
- The output appears to represent a normalized or scaled-down version of the fill ratio within the bounded region

Key questions:
- Is there a clear frame/boundary structure in the input?
- Does the frame contain both filled and unfilled portions?
- Is the output significantly smaller than the input?
- Does the output seem to represent the proportional fill of the bounded area?

Answer ONLY with: YES or NO"""
