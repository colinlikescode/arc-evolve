CLASSIFIER_PROMPT = """Does this puzzle exhibit CROSS INTERSECTION HIGHLIGHTING?

Cross intersection highlighting means:
- The input contains two perpendicular lines (one horizontal, one vertical) that intersect
- Each line spans most or all of the grid in its direction
- The lines are made of different non-background colors
- The transformation adds a highlight region around the intersection point

Look at the training examples:
- Is there a vertical line of one color running through the grid?
- Is there a horizontal line of a different color running through the grid?
- Do these lines intersect at exactly one point?
- In the output, is there a new color (like a marker/highlight) forming a small region around that intersection?
- Does the highlight form a 3x3 area centered on the intersection, replacing background cells?

Answer ONLY with: YES or NO"""
