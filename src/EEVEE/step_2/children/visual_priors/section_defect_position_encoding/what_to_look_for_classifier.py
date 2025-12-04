CLASSIFIER_PROMPT = """Does this puzzle involve SECTION DEFECT POSITION ENCODING?

This pattern means:
- The input grid is divided into multiple vertical sections by separator columns (a single column of a marker color)
- Each section may contain a small rectangular "defect" or "hole" (cells of the marker color embedded within the background)
- The output is a small grid where each row corresponds to one section
- The color of each output row encodes the VERTICAL POSITION of the defect within that section
- Different vertical positions map to different output colors

Look at the training examples:
- Is the input horizontally divided into equal-width sections by single separator columns?
- Does each section have a small embedded pattern (like a 2x2 block) at varying vertical positions?
- Is the output a small grid with uniform-color rows?
- Does the output row color seem to depend on where the embedded pattern appears vertically in each section?

Answer ONLY with: YES or NO"""
