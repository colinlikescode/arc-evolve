CLASSIFIER_PROMPT = """Does this puzzle involve IDENTIFYING AND RECOLORING THE LARGEST CONNECTED COMPONENT?

Look for these indicators:
- The input contains scattered non-zero cells forming distinct connected regions (using 4-connectivity: up, down, left, right)
- The output has the same grid structure with cells in the same positions
- One group of connected non-zero cells has been recolored to a different non-zero color
- The recolored region appears to be the LARGEST connected component by cell count
- Smaller connected components and isolated cells retain their original color

Check the training examples:
- Are there multiple separate groups of connected non-zero cells in each input?
- Does exactly one group change color in each output?
- Is the group that changes color consistently the largest connected region?

Answer ONLY with: YES or NO"""
