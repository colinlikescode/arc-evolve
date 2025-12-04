CLASSIFIER_PROMPT = """Does this puzzle exhibit CONCENTRIC LAYER INVERSION?

Concentric layer inversion means:
- The input grid has a nested/layered structure with different colors forming concentric rectangular rings (like an onion or nested frames)
- Each layer/ring surrounds the next inner layer
- The output has the SAME structure but with the layer colors REVERSED (innermost becomes outermost, outermost becomes innermost)

Look at the training examples:
- Does the input have multiple concentric rectangular frames/borders of different colors?
- Is there a clear center region surrounded by progressively larger frames?
- Does the output maintain the same geometric structure but with colors swapped inside-out?
- Does the outermost color in the input become the innermost color in the output, and vice versa?

Answer ONLY with: YES or NO"""
