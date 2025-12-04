CLASSIFIER_PROMPT = """Does this puzzle exhibit CORNER MARKER EXTRACTION AND REFLECTION?

This pattern involves:
- A rectangular frame/border made of a single color in the input
- Inside the frame, there are colored markers in the corner regions (typically 4 distinct colored cells near the corners)
- The interior of the frame (excluding the markers) may have some empty/background cells

The transformation:
- The colored corner markers are REMOVED from inside the frame
- Each marker is REFLECTED/PROJECTED outward to a position OUTSIDE the frame
- The reflection is diagonal: each corner marker moves to the diagonally opposite external corner position relative to the frame
- The frame structure itself is preserved but its interior becomes empty

Look at the training examples:
- Is there a rectangular border/frame made of one color?
- Are there exactly 4 colored markers positioned near the inner corners of the frame?
- In the output, are these markers moved outside the frame to diagonally reflected positions?
- Is the frame's interior cleared of the original markers?

Answer ONLY with: YES or NO"""
