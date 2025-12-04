CLASSIFIER_PROMPT = """Does this puzzle involve RANKING COLORED REGIONS BY SIZE?

Look for these indicators:
- The input contains multiple distinct colored regions (clusters of non-zero cells) on a zero/background
- Each region is a different color and varies in size (number of cells)
- The output is a single column (Nx1) where N equals the number of distinct colored regions
- The output lists the colors in a specific order based on their region sizes

Check the training examples:
- Are there multiple separate colored blobs/regions in the input?
- Does the output height match the number of distinct colors/regions?
- Does the output appear to order the colors by the size (cell count) of each region?
- Is the ordering from largest to smallest (or vice versa)?

Answer ONLY with: YES or NO"""
