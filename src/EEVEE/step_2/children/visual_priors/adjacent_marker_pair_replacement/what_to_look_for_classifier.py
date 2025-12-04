CLASSIFIER_PROMPT = """Does this puzzle involve ADJACENT MARKER PAIR REPLACEMENT?

This pattern means:
- Two distinct non-background colors act as "markers" that appear in adjacent pairs (horizontally or vertically touching)
- When these two marker colors are found adjacent to each other, one is replaced with a NEW color and the other is removed (set to background)
- Other colors in the grid (anchors) remain unchanged
- The same marker color can appear multiple times, but only instances adjacent to the other marker color are affected

Look at the training examples:
- Are there two specific colors that frequently appear next to each other?
- Do these adjacent pairs get modified while isolated instances may remain?
- Does a new color appear in the output that wasn't in the input?
- Do some colors remain completely unchanged throughout?

Answer ONLY with: YES or NO"""
