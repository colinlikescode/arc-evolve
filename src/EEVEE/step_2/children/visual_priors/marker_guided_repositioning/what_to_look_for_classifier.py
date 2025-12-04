CLASSIFIER_PROMPT = """Does this puzzle exhibit MARKER-GUIDED OBJECT REPOSITIONING?

Marker-guided object repositioning means:
- There is a central object/shape made of one color (the "main object")
- There are scattered single-cell markers of a different color around the grid
- The markers act as "anchor points" that need to be repositioned relative to the main object
- In the output, the main object stays in place (or moves slightly)
- The markers are moved to positions adjacent to or near the main object
- The relative direction/distance of each marker from the object determines its new position around the object

Look at the training examples:
- Is there a small rectangular object (like a 2x2 block) in the grid?
- Are there isolated single cells of a different color scattered around?
- In the output, do those scattered markers move to surround or be adjacent to the main object?
- Does each marker's original direction from the object determine where it ends up relative to the object?

Answer ONLY with: YES or NO"""
