CLASSIFIER_PROMPT = """Does this puzzle involve GRID PARTITIONING WITH DENSITY-BASED COLOR MAPPING?

Look for these indicators:
- The input grid is divided into rectangular regions/blocks by separator lines (typically rows/columns of zeros)
- Each region is filled predominantly with ONE non-zero color, with some cells being zero (holes/gaps)
- Multiple distinct colored regions exist, arranged in a grid-like pattern
- The output is a small grid where each cell represents one region from the input
- The output dimensions correspond to the number of region rows × number of region columns

Key observations:
- Are there clear horizontal and/or vertical separator lines (all zeros) dividing the grid?
- Does each partitioned region have a dominant non-zero color with scattered zero cells?
- Is the output much smaller than the input (condensed representation)?
- Does each output cell seem to represent the dominant color of a corresponding input region?

Answer ONLY with: YES or NO"""
