CLASSIFIER_PROMPT = """Does this puzzle exhibit RECTANGLE INTERIOR FILLING?

Rectangle interior filling means:
- The input contains one or more solid rectangular regions of a non-background color
- Each rectangle is filled uniformly with the same color
- The output keeps the outer border (1-cell thick edge) of each rectangle unchanged
- The interior of each rectangle (all cells not on the border) is filled with a different "fill" color

Look at the training examples:
- Are there distinct solid rectangular regions in the input?
- In the output, do these rectangles maintain their original color only on the edges?
- Is the interior (non-border cells) of each rectangle replaced with a new uniform color?
- Does the fill pattern respect the shape - smaller rectangles may have smaller or no interior?

Answer ONLY with: YES or NO"""
