CLASSIFIER_PROMPT = """Does this puzzle exhibit RECTANGULAR REGION OVERLAP FILLING?

This pattern involves:
- Two or more distinct colored rectangular regions on a background
- The regions are separated by a gap filled with background color
- The gap between regions gets filled with a NEW color (often a specific "fill" color)
- The fill region is the INTERSECTION of the row/column spans of the two colored rectangles

Look at the training examples:
- Are there exactly two colored rectangular blocks on a background?
- Is there a gap (background-colored region) between them?
- In the output, is part of that gap filled with a new color?
- Does the filled region correspond to where the horizontal span of one rectangle overlaps with the vertical span of the other (or vice versa)?

Answer ONLY with: YES or NO"""
