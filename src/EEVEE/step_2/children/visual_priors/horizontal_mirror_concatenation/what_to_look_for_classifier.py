CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL MIRROR CONCATENATION?

Horizontal mirror concatenation means:
- The output width is exactly 2× the input width
- The output height equals the input height
- The output consists of the original input placed on the left
- The right half is a horizontally flipped (mirror) copy of the input

Look at the training examples:
- Is the output exactly twice as wide as the input?
- Does the left half of the output match the input exactly?
- Does the right half appear to be the input reversed left-to-right (each row reversed)?
- Is each output row formed by: [original row] + [reversed original row]?

Answer ONLY with: YES or NO"""
