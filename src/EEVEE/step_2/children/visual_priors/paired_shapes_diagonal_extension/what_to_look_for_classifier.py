CLASSIFIER_PROMPT = """Does this puzzle exhibit PAIRED SHAPES WITH DIAGONAL LINE CONNECTIONS?

This pattern involves:
- Two or more small shapes/clusters of the same non-zero color in the input
- The shapes appear to be rotations or reflections of each other (like matching "corners" or "L-shapes")
- In the output, diagonal lines of the same color are drawn connecting the shapes
- The diagonal lines extend from the "open" or "pointed" ends of each shape toward the other shape(s)

Look at the training examples:
- Are there multiple small clusters of the same color scattered in the grid?
- Do the shapes look like they could "point" toward each other?
- In the output, are there new diagonal trails of single cells connecting or extending from these shapes?
- Do the diagonal lines emanate from specific corners/tips of each shape?

Answer ONLY with: YES or NO"""
