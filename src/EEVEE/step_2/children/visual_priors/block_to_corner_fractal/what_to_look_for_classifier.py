CLASSIFIER_PROMPT = """Does this puzzle exhibit BLOCK-TO-CORNER FRACTAL REDUCTION?

This pattern means:
- The input contains multiple solid rectangular blocks of uniform size arranged on a grid
- The blocks form a meta-pattern (like a 3x3 arrangement of block positions)
- The output size equals the number of block positions times the block dimensions
- Each filled block in the input becomes a "corner pattern" in the output (non-zero at corners/edges, zero at center)
- Each empty block position in the input becomes all zeros in the output

Look at the training examples:
- Is the input made of uniformly-sized solid rectangular blocks?
- Do the blocks form a regular grid arrangement (like 3x3 block positions)?
- Is the output a grid where filled input blocks become sparse corner patterns?
- Do empty input block positions correspond to all-zero blocks in the output?

Answer ONLY with: YES or NO"""
