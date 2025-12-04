CLASSIFIER_PROMPT = """Does this puzzle involve CROSS REPOSITIONING based on MARKER LOCATION?

Look for these indicators:
- The input contains a cross/plus shape made of one color (a vertical line and horizontal line intersecting)
- There is a MARKER color (different from the cross color) appearing in a specific quadrant or edge region
- The marker cells indicate which quadrant the cross intersection should be moved to
- The output has the same cross shape but with the intersection point relocated

Specifically check:
- Is there a full-width horizontal line and a full-height vertical line of the same non-background color?
- Is there a secondary color (marker) appearing only in certain cells, typically near an edge or corner?
- Does the output show the cross repositioned so the intersection moves toward where the markers were?
- Are the markers removed in the output?

Answer ONLY with: YES or NO"""
