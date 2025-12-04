CLASSIFIER_PROMPT = """Does this puzzle exhibit PATH FLOODING WITH ALTERNATING COLORS?

Look for these indicators:
- The grid has a dominant "wall" color and empty/path cells (a different value)
- There is a small cross or plus-shaped seed pattern made of TWO distinct colors (neither the wall nor path color)
- The seed pattern has alternating colors (like A-B-A horizontally and vertically from a center)
- In the output, these two colors propagate outward along connected paths of empty cells
- The propagation maintains an alternating pattern (like a checkerboard) as it extends

Key observations:
- Is there a small 3-cell cross pattern with two alternating non-background colors?
- Are there corridors of empty cells that could act as paths?
- Does the output show these colors extending along the empty paths while alternating?

Answer ONLY with: YES or NO"""
