CLASSIFIER_PROMPT = """Does this puzzle involve SELECTING THE CORRECT SHAPE from multiple candidate shapes using a MARKER CELL?

Look for these indicators:
- The input contains multiple separate clusters/shapes of the same non-background color
- There is a single cell of a DIFFERENT unique color (a marker/indicator cell)
- The marker cell is positioned near or adjacent to ONE of the shapes
- The output is a small grid containing just ONE of the shapes from the input
- The output shape corresponds to the shape that the marker cell is closest to or pointing at

Key questions:
- Are there multiple disconnected regions of the same color in the input?
- Is there exactly one cell of a distinct "marker" color?
- Does the output appear to be an extracted/cropped version of one specific shape?
- Is the marker cell spatially associated with the shape that becomes the output?

Answer ONLY with: YES or NO"""
