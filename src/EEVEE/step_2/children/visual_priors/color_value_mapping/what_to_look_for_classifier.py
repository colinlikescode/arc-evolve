CLASSIFIER_PROMPT = """Does this puzzle exhibit a COLOR MAPPING / VALUE SUBSTITUTION pattern?

Color mapping means:
- Each unique color/value in the input is consistently replaced with a different specific color/value in the output
- The spatial structure and positions remain IDENTICAL - only the colors change
- The same input color always maps to the same output color across all cells
- This is a one-to-one mapping function applied to each cell independently

Look at the training examples:
- Does the grid structure (shape, positions) stay exactly the same between input and output?
- Is each distinct input color consistently replaced by a single distinct output color?
- Do repeated rows/columns in the input remain repeated (with new colors) in the output?
- Is there NO spatial transformation (no rotation, reflection, scaling, or rearrangement)?

Answer ONLY with: YES or NO"""
