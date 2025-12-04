CLASSIFIER_PROMPT = """Does this puzzle exhibit a SPLIT-GRID XOR COMPARISON pattern?

This pattern involves:
- The input grid is divided into TWO REGIONS by a horizontal separator line (a row filled with a distinct "divider" color)
- The two regions above and below the separator have the same dimensions
- Both regions contain a mix of a "primary" color and a "background" color (typically black/zero)
- The output grid has the same dimensions as ONE of the regions
- The output appears to mark cells where EXACTLY ONE of the two regions has the primary color (XOR logic)
- Cells where both regions match (both primary or both background) become background in output
- Cells where they differ get marked with a NEW "result" color

Look at the training examples:
- Is there a horizontal line of a uniform color dividing the grid into two equal halves?
- Do the top and bottom halves have the same width and height?
- Does the output size match one half of the input?
- Does the output show a comparison result between the two halves?

Answer ONLY with: YES or NO"""
