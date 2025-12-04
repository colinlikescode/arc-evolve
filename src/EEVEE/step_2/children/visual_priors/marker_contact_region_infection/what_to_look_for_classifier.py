CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER CONTACT REGION INFECTION?

This pattern means:
- The input has MARKER cells (one color, like blue) and REGION cells (another color, like red)
- Markers SPREAD/PROPAGATE outward (horizontally and/or vertically as rays or lines)
- When a spreading marker TOUCHES or CONTACTS a region (even by side adjacency), it INFECTS that region
- The entire connected region that was touched gets filled/converted to the marker color
- It's like a contagion: markers spread, and any region they touch gets "infected" and filled

Look at the training examples:
- Are there scattered marker cells (single color) and larger region shapes (different color)?
- Do the markers appear to extend/spread outward in the output?
- When a marker or its extension TOUCHES a region, does that ENTIRE region get filled with the marker color?
- Is contact/adjacency the trigger for filling a region?
- Do regions that are NOT touched by markers remain unchanged?

Answer ONLY with: YES or NO"""
