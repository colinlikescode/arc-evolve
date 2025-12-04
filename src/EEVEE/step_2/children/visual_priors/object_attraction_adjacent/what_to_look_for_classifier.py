CLASSIFIER_PROMPT = """Does this puzzle involve MOVING ONE OBJECT TO BE ADJACENT TO ANOTHER STATIONARY OBJECT?

Look for these indicators:
- There are exactly TWO distinct non-background objects in the grid
- One object is smaller and compact (often a 2x2 square) - this is the "anchor"
- One object is larger or more irregular - this is the "movable" object
- In the output, the movable object has been repositioned to be directly adjacent to the anchor
- The anchor object remains in its original position
- The movable object maintains its shape but changes location
- The direction of movement is toward the anchor (closing the gap between them)

This is NOT about rotation, reflection, or scaling - just translation/movement.

Answer ONLY with: YES or NO"""
