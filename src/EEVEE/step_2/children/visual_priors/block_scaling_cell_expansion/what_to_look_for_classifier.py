CLASSIFIER_PROMPT = """Does this puzzle exhibit BLOCK SCALING / CELL EXPANSION?

Block scaling means:
- The input is a small grid (e.g., N×M)
- The output is exactly N times larger in each dimension (N×N by M×M for an N×M input)
- Each individual CELL in the input becomes a BLOCK of identical values in the output
- The block size equals the input dimensions (each cell expands to an N×M block)
- The color/value of each cell is preserved and fills its entire expanded block

Look at the training examples:
- Is the output exactly input_height × input_height rows and input_width × input_width columns?
- Does each cell in the input correspond to a uniform block of the same color in the output?
- Are the blocks arranged in the same spatial pattern as the original cells?
- Is every cell (including zeros/background) expanded uniformly?

Answer ONLY with: YES or NO"""
