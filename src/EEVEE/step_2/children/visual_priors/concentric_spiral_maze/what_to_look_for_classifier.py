CLASSIFIER_PROMPT = """Does this puzzle exhibit a CONCENTRIC SPIRAL/RECTANGULAR MAZE pattern?

This pattern means:
- The input is a uniform grid filled entirely with the background color (all zeros)
- The output draws nested rectangular rings that spiral inward from the edges
- The pattern alternates between a non-background color and the background color
- Starting from the outer edge, the first row is filled with a non-background color
- The spiral continues inward, alternating colors every 2 rows/columns to create a maze-like nested rectangle pattern
- The direction of the spiral creates an effect like walking through concentric rectangular frames

Look at the training examples:
- Is the input grid completely uniform (all one color)?
- Does the output show nested rectangular borders spiraling inward?
- Do the rings alternate between two colors (the original background and a new color)?
- Does the pattern resemble a rectangular maze or concentric frames?

Answer ONLY with: YES or NO"""
