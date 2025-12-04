CLASSIFIER_PROMPT = """Does this puzzle involve QUADRANT COLOR MAPPING using a small color key?

Look for these indicators:
- The input grid is divided by a separator line (horizontal and vertical) into distinct regions
- One region contains a small 2x2 block of different colors (the "color key")
- Another larger region contains a pattern made with a single marker/template color
- The pattern region appears to be logically divided into quadrants (2x2 arrangement of sub-regions)
- The output is smaller than the input and shows the pattern with the marker color replaced
- Each quadrant of the pattern uses a different color from the 2x2 key

The transformation maps each position in the 2x2 color key to the corresponding quadrant of the pattern, replacing the marker color with that key color.

Answer ONLY with: YES or NO"""
