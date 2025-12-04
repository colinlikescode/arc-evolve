CLASSIFIER_PROMPT = """Does this puzzle exhibit SIMPLE COLOR SUBSTITUTION?

Simple color substitution means:
- The input and output grids have exactly the same dimensions
- The spatial pattern/structure remains completely unchanged
- One specific color in the input is replaced with a different color in the output
- All other colors remain exactly the same in their original positions

Look at the training examples:
- Do the input and output have identical grid sizes?
- Is the pattern of cells (which cells are which) preserved?
- Does it appear that exactly one color has been swapped for another?
- Are all other colors unchanged between input and output?

Answer ONLY with: YES or NO"""
