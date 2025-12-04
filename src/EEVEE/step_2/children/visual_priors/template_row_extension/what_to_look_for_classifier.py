CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE-BASED ROW EXTENSION?

Template-based row extension means:
- One row in the input spans the full width with a complete non-zero pattern (the "template row")
- Other rows have partial patterns (non-zero values only in the first few columns, zeros elsewhere)
- The partial rows need to be extended to full width following the template row's structural pattern
- The template defines which positions share the same "role" (same values in template = same role)
- Each partial row's distinct colors get mapped to fill the full row according to the template's positional structure

Look at the training examples:
- Is there one row that spans the full grid width with non-zero values?
- Are there other rows with non-zero values only at the start, followed by zeros?
- In the output, do those partial rows get extended to full width?
- Does the extension follow the same positional pattern as the template row?

Answer ONLY with: YES or NO"""
