CLASSIFIER_PROMPT = """Does this puzzle exhibit REPEATING TILE EXTRACTION?

Repeating tile extraction means:
- The input grid contains a pattern that is repeated/tiled multiple times
- The same sub-pattern appears 2 or more times either horizontally, vertically, or both
- The output is the SINGLE UNIT TILE (the smallest repeating block)
- The input dimensions are exact multiples of the output dimensions

Look at the training examples:
- Is the input grid composed of identical repeating blocks?
- Can you identify a tile that, when repeated, recreates the entire input?
- Is the output smaller than the input by a factor that divides evenly?
- Does the pattern repeat along one axis (horizontal OR vertical) or both?

Answer ONLY with: YES or NO"""
