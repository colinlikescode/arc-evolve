CLASSIFIER_PROMPT = """Does this puzzle exhibit LINE EXTENSION WITH INTERSECTION MARKING?

This pattern involves:
- Two distinct line segments or partial lines in the input, oriented perpendicular to each other (one vertical, one horizontal)
- Each line segment is made of a single non-background color
- The lines are short/partial and do not span the full grid

The transformation:
- Each line is extended across the entire grid in its respective direction
- Where the two extended lines intersect, a special "intersection marker" color appears
- The intersection cell gets a unique color different from both line colors

Look at the training examples:
- Is there a short vertical line segment (same color in a column)?
- Is there a short horizontal line segment (different color in a row)?
- In the output, do both lines extend fully across the grid?
- Is there a special color at the intersection point?

Answer ONLY with: YES or NO"""
