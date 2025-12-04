CLASSIFIER_PROMPT = """Does this puzzle exhibit OBJECT RELOCATION TO BOUNDARY WITH TRAIL MARKER?

This pattern involves:
- A distinct object/shape made of one color
- A boundary line (row or column) made of a different color that spans the full width/height
- The object is moved from its original position to be adjacent to the boundary line
- A new marker line appears at the object's original position (or edge of where it was)
- The object is placed on the side of the boundary that is closer to its original position

Look at the training examples:
- Is there a solid line (row or column) of one color acting as a boundary?
- Is there a distinct shape/pattern made of another color somewhere else in the grid?
- In the output, does the shape move to be adjacent to the boundary line?
- Does a new line appear marking where the object originally was (or its edge)?
- Is the original location of the shape cleared (filled with background)?

Answer ONLY with: YES or NO"""
