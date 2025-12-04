CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID-BASED CELL COLORING WITH DEFECT DETECTION?

This pattern involves:
- A grid divided into rectangular cells by horizontal and vertical separator lines (using a single non-background color)
- The separator lines form a regular grid pattern, creating uniform rectangular cells
- Some separator line positions have "defects" - gaps where the separator color is missing (replaced by background)
- The transformation fills each cell with one of two fill colors based on whether the cell contains any defects (missing separator segments on its borders)
- Cells that are "clean" (no defects on their borders) get one fill color
- Cells that have defects (gaps in the separator lines along their edges) get a different fill color
- The separator lines themselves are preserved, with defect positions also being filled with the defect-indicator color

Look at the training examples:
- Is there a regular grid structure with separator lines dividing the grid into cells?
- Are there occasional gaps/breaks in the separator lines?
- In the output, are cells filled with different colors based on their proximity to these gaps?
- Do the separator lines remain intact (with gaps getting a specific fill color)?

Answer ONLY with: YES or NO"""
