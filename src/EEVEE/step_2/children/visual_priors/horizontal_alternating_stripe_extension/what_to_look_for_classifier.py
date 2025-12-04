CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL ALTERNATING EXTENSION from isolated colored cells?

This pattern means:
- The input contains isolated non-zero colored cells scattered on a background of zeros
- Each isolated colored cell becomes the starting point of a horizontal stripe
- The stripe extends from the cell's position to the RIGHT edge of the grid
- The stripe alternates between the original cell's color and a fixed "separator" color
- The pattern is: original_color, separator_color, original_color, separator_color, ...
- The row position and starting column of each colored cell are preserved

Look at the training examples:
- Are there isolated single colored cells in the input?
- Does each colored cell spawn a horizontal line extending rightward?
- Does the line alternate between two colors (the original color and one consistent separator color)?
- Do the stripes extend all the way to the right edge of the grid?

Answer ONLY with: YES or NO"""
