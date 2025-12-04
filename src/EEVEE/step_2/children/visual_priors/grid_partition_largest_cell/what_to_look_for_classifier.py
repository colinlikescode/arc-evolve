CLASSIFIER_PROMPT = """Does this puzzle involve GRID LINE PARTITIONING AND LARGEST CELL EXTRACTION?

Grid line partitioning means:
- The input grid contains horizontal and/or vertical lines made of a single "divider" color
- These lines span the entire width or height of the grid
- The lines divide the grid into rectangular cells/regions
- The cells between the divider lines vary in size

Look at the training examples:
- Are there complete rows or columns filled with a single color that act as dividers?
- Do these divider lines create a grid-like partition of the space?
- Are the resulting rectangular regions different sizes?
- Is the output a solid rectangle filled with the non-divider (background/fill) color?
- Does the output size correspond to the dimensions of the LARGEST rectangular cell?

Answer ONLY with: YES or NO"""
