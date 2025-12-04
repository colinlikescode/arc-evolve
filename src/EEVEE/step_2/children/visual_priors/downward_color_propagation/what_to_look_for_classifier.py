CLASSIFIER_PROMPT = """Does this puzzle exhibit DOWNWARD COLOR PROPAGATION / GRAVITY FILL?

Downward color propagation means:
- Non-zero colored cells in each column "fall" or propagate downward
- Each column is processed independently
- Non-zero values fill in the zero cells below them, extending to the bottom of the grid
- The original non-zero cells remain in place
- Zero cells that are below a non-zero cell get filled with that non-zero value

Look at the training examples:
- Does each column have at most one or two distinct non-zero colors?
- Do the non-zero colors appear to extend/propagate downward from their original position?
- Are the zero cells below colored cells being filled with those colors?
- Does the top row remain unchanged while lower rows gain colors?

Answer ONLY with: YES or NO"""
