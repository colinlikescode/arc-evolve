CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE FILLING WITH PATTERN TRANSFER?

This pattern involves:
- Multiple rectangular regions bounded by a specific "frame" color (forming closed rectangular outlines)
- Some framed regions contain "holes" (cells with the background color inside the frame)
- Outside the framed regions, there are small colored patterns/shapes scattered in the grid
- The transformation fills the holes inside framed regions with patterns found elsewhere

Look at the training examples:
- Are there rectangular regions outlined by a consistent frame color?
- Do some framed regions have internal holes (background-colored cells inside)?
- Are there small colored patterns outside the framed regions?
- In the output, are the holes filled with colors from patterns found elsewhere?
- Do the scattered patterns outside frames get "cleaned up" (removed) in the output?

Answer ONLY with: YES or NO"""
