CLASSIFIER_PROMPT = """Does this puzzle exhibit DIAGONAL TRAIL EXTENSION FROM PAIRED BLOCKS?

This pattern involves:
- Two distinct colored rectangular blocks (typically 2x2) in the input
- Each block remains in place in the output
- Diagonal single-pixel trails extend from each block toward opposite corners of the grid
- The block closer to the top-left corner extends a trail toward the top-left
- The block closer to the bottom-right corner extends a trail toward the bottom-right
- Trails use the same color as their source block

Look at the training examples:
- Are there exactly two distinct colored blocks in the input?
- Do diagonal lines of single pixels appear in the output extending from each block?
- Do the trails extend toward opposite corners (top-left and bottom-right)?
- Does each trail match the color of its originating block?

Answer ONLY with: YES or NO"""
