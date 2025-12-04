CLASSIFIER_PROMPT = """Does this puzzle involve a LOGICAL XOR COMPARISON between two separated grid regions?

Look for these indicators:
- The input grid is divided into two equal-sized regions by a horizontal separator row (a row filled with a single uniform color)
- Each region above and below the separator contains a binary pattern (non-zero vs zero, or two distinct values)
- The output grid is the same size as one of these regions
- The output marks positions where EXACTLY ONE of the two input regions has a non-background/non-zero value (exclusive OR)
- Positions where both regions match (both filled or both empty) show background in the output
- Positions where the regions differ show a marked/colored cell in the output

The transformation compares two stacked grids cell-by-cell and outputs their logical difference.

Answer ONLY with: YES or NO"""
