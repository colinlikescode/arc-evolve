CLASSIFIER_PROMPT = """Does this puzzle exhibit CONCENTRIC FRAME INVERSION (inside-out reversal)?

Concentric frame inversion means:
- The input grid has nested rectangular frames/rings of different colors
- Each frame is a 1-cell thick border surrounding inner content
- The frames form concentric layers from outside to inside
- The transformation REVERSES the order of these layers
- The outermost frame color becomes the innermost, and vice versa
- Middle layers also swap positions symmetrically

Look at the training examples:
- Does the input have a "nested boxes" or "concentric frames" structure?
- Are there multiple distinct colors forming rectangular rings?
- In the output, has the layer ordering been reversed (outside becomes inside)?
- Does the grid maintain the same size but with colors redistributed by layer?

Answer ONLY with: YES or NO"""
