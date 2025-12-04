CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL REFLECTION TILING / PALINDROME ROW EXPANSION?

This pattern means:
- The input is a rectangular grid with a repeating horizontal pattern
- The output has the SAME WIDTH as the input but INCREASED HEIGHT
- The output is created by taking the input rows and reflecting them vertically
- The pattern creates a palindrome-like structure: the input rows are followed by their vertical mirror (excluding duplicating boundary rows)
- The first and last rows of the input appear as "anchor" rows, with middle rows reflected between them

Look at the training examples:
- Does the output width match the input width exactly?
- Is the output height larger than the input height?
- Do the rows of the output form a vertically symmetric/palindromic pattern?
- Does the input pattern repeat and reflect to create the output?
- Are the first and last rows of the input serving as boundaries that get repeated in a mirrored fashion?

Answer ONLY with: YES or NO"""
