CLASSIFIER_PROMPT = """Does this puzzle exhibit NESTED STAIRCASE/L-SHAPE CONTINUATION?

This pattern means:
- The input contains a partial connected shape made of non-zero cells
- The shape forms a "staircase" or nested L-shaped structure with steps of varying lengths
- The output fills the ENTIRE grid by continuing this staircase pattern
- The continuation alternates between the original non-zero color and a fill/background color
- The result is a complete nested pattern covering the whole grid

Look at the training examples:
- Is there a connected non-zero shape that looks like stairs or nested L-shapes?
- Does the shape have "steps" that increase or decrease in length?
- Does the output show the same staircase pattern extended to fill the entire grid?
- Are there two colors in the output: the original non-zero color and a new fill color?

Answer ONLY with: YES or NO"""
