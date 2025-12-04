CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE STAMPING onto placeholder regions?

Template stamping means:
- There is ONE multi-colored pattern/template somewhere in the grid (contains 2+ distinct non-background colors)
- There are multiple UNIFORM rectangular regions filled with a single "placeholder" color
- The placeholder regions have the SAME dimensions as the template pattern
- In the output, each placeholder region is REPLACED with a copy of the template pattern
- The original template remains unchanged in its position

Look at the training examples:
- Is there exactly one region with a complex multi-color pattern?
- Are there other regions filled uniformly with a single non-background color?
- Do the uniform regions match the size of the complex pattern?
- In the output, are all uniform regions replaced with copies of the complex pattern?

Answer ONLY with: YES or NO"""
