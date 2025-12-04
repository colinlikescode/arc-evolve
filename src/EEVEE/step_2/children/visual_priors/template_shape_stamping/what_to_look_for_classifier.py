CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE STAMPING / PATTERN BROADCASTING?

Template stamping means:
- The input contains a "template shape" defined by one specific color (often appearing as a connected pattern)
- The input also contains other scattered colored cells at various positions
- The output is larger than the input, scaled by the template dimensions
- Each non-template colored cell from the input appears in the output as a COPY of the template shape, but filled with that cell's color
- The template shape is "stamped" at positions corresponding to where each colored cell was located

Look at the training examples:
- Is there one color that forms a distinct shape/pattern (the template)?
- Are there other colors appearing as individual cells or small clusters?
- Is the output significantly larger than the input?
- Does each non-template color appear multiple times in the output, forming the same shape as the template?
- Are these stamped shapes positioned according to where the original colored cells were?

Answer ONLY with: YES or NO"""
