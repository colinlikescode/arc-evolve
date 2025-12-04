CLASSIFIER_PROMPT = """Does this puzzle exhibit EXTRACT AND TILE HORIZONTALLY pattern?

This pattern means:
- The input contains a small connected shape made of non-zero cells on a background of zeros
- The output extracts just the bounding box of this shape
- The extracted shape is then tiled/duplicated horizontally (placed side by side)
- The output width is exactly 2× the width of the extracted shape's bounding box
- The output height equals the height of the extracted shape's bounding box

Look at the training examples:
- Is there a single connected colored shape in the input grid?
- Is the output much smaller than the input (cropped to the shape)?
- Does the output appear to be the same shape repeated twice horizontally?
- Is the output width double what you'd expect from just extracting the shape?

Answer ONLY with: YES or NO"""
