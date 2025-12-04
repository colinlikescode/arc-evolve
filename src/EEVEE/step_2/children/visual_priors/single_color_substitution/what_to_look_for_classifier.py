CLASSIFIER_PROMPT = """Does this puzzle exhibit SINGLE COLOR SUBSTITUTION?

Single color substitution means:
- The input and output grids have the same dimensions
- One specific color in the input is consistently replaced with a different color in the output
- All other colors remain unchanged in their original positions
- The replacement is global - every instance of the target color is changed

Look at the training examples:
- Are the input and output grids the same size?
- Is there exactly one color that appears in the input but NOT in the output?
- Is there exactly one color that appears in the output but NOT in the input?
- Do all other colors stay in exactly the same positions?

Answer ONLY with: YES or NO"""
