CLASSIFIER_PROMPT = """Does this puzzle involve FINDING THE ODD QUADRANT OUT?

Look for these indicators:
- The input grid is divided into quadrants by a row and/or column of zeros (acting as separators)
- The separators split the grid into four equally-sized rectangular regions
- Three of the four quadrants appear identical or very similar
- One quadrant is different from the others
- The output is a small grid matching the size of one quadrant

Check:
- Is there a clear dividing line (row/column of zeros) splitting the grid?
- Are most quadrants identical with one being different?
- Is the output size equal to the quadrant size?

Answer ONLY with: YES or NO"""
