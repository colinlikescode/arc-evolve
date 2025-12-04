CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING A SUBREGION AND REPLACING BACKGROUND?

Look for these indicators:
- The input has a dominant "background" color filling most of the grid
- There is a smaller region/pattern made of non-background colors embedded in the grid
- The output is smaller than the input - it appears to be a cropped/extracted region
- The output contains the non-background colored cells from the input
- Any cells that were the background color WITHIN the extracted region become a different color (typically black/zero) in the output

Key characteristics:
- The output dimensions match the bounding box of the non-background pattern in the input
- Non-background colors are preserved in their relative positions
- Background color cells that fall within the bounding box are converted to zero/black

Answer ONLY with: YES or NO"""
