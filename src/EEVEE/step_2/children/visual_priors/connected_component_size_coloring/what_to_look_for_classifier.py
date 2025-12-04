CLASSIFIER_PROMPT = """Does this puzzle involve CONNECTED COMPONENT LABELING with SIZE-BASED COLORING?

This pattern means:
- The input contains multiple separate connected components (clusters) of the same non-zero color
- In the output, each distinct connected component is assigned a unique color
- The color assignment is based on the SIZE of each cluster (number of cells)
- Larger clusters receive one color, smaller clusters receive different colors

Look at the training examples:
- Is there a single non-zero color in the input forming multiple disconnected regions?
- Does each separate region get recolored with a different color in the output?
- Do the colors appear to correlate with the relative sizes of the clusters?
- Are the shapes/positions of clusters preserved, only colors changed?

Answer ONLY with: YES or NO"""
