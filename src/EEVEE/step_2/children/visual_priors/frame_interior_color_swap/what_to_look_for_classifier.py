CLASSIFIER_PROMPT = """Does this puzzle exhibit FRAME-INTERIOR COLOR SWAP?

Frame-interior color swap means:
- The input contains a rectangular shape on a background
- The shape has a "frame" or "border" made of one color
- The shape has an "interior" or "center" made of a different color
- The output extracts just this shape (cropped from the background)
- In the output, the frame color and interior color are SWAPPED

Look at the training examples:
- Is there a rectangular region with two distinct non-background colors?
- Does one color form the outer border/frame of the rectangle?
- Does another color fill the interior/center of the rectangle?
- Is the output a cropped version of this rectangle with the two colors swapped?
- Is the background (typically the most common color) removed entirely?

Answer ONLY with: YES or NO"""
