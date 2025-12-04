CLASSIFIER_PROMPT = """Does this puzzle exhibit ROW-WISE COLUMN POSITION MAPPING?

This pattern means:
- Each row in the input contains exactly one marker cell (non-zero/non-background)
- The COLUMN POSITION of that marker determines what color fills the entire output row
- Each output row is filled uniformly with a single color
- The mapping is: column index → specific output color (e.g., leftmost column → one color, middle column → another color, rightmost column → a third color)

Look at the training examples:
- Does each input row have exactly one non-background cell?
- Is each output row filled with a single uniform color?
- Do rows with markers in the same column position get the same output color?
- Does the column position of the marker (not its color) determine the output row's color?

Answer ONLY with: YES or NO"""
