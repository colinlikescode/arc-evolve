CLASSIFIER_PROMPT = """Does this puzzle involve CENTERING A PATTERN WITHIN A MARKER-DEFINED FRAME?

Look for these indicators:
- Are there exactly 4 cells of one distinct color forming corners of a rectangle?
- Is there a shape/pattern made of another non-background color inside or near this frame?
- Does the output show the same pattern repositioned (centered) within the bounds of the corner markers?
- Do the corner markers remain fixed in both input and output?

The transformation centers or repositions a pattern horizontally (and possibly vertically) within the rectangular region defined by corner markers.

Answer ONLY with: YES or NO"""
