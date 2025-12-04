CLASSIFIER_PROMPT = """Does this puzzle exhibit a CHECKERBOARD INTERLEAVING pattern?

Checkerboard interleaving means:
- The input consists of exactly 2 rows, where each row contains a single uniform color
- The output has the same dimensions as the input
- The two colors from the input rows are interleaved in a checkerboard pattern
- In the output, adjacent cells (horizontally and vertically) alternate between the two colors
- The pattern follows: output[row][col] uses one color if (row + col) is even, and the other color if (row + col) is odd

Look at the training examples:
- Does the input have exactly 2 rows with each row being a single solid color?
- Does the output create a checkerboard pattern using those two colors?
- Do horizontally and vertically adjacent cells have different colors in the output?

Answer ONLY with: YES or NO"""
