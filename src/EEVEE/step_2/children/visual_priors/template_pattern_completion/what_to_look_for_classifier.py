CLASSIFIER_PROMPT = """Does this puzzle exhibit PATTERN COMPLETION BY REFERENCE TO A TEMPLATE?

This pattern type involves:
- A "complete" template pattern that spans the full width (or height) of the grid
- Multiple "incomplete" versions of a similar pattern elsewhere in the grid
- The incomplete patterns have the same structure/shape as the template but are truncated or cut short
- The transformation fills in the missing portions of incomplete patterns using a secondary color

Look at the training examples:
- Is there one instance of a pattern that extends fully across the grid?
- Are there other instances of similar patterns that stop partway across?
- In the output, are the incomplete patterns extended to match the template's extent?
- Is a different color used to fill in the extended portions?

Answer ONLY with: YES or NO"""
