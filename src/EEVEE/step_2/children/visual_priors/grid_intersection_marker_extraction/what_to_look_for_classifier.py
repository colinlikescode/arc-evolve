CLASSIFIER_PROMPT = """Does this puzzle exhibit GRID-TO-SUMMARY EXTRACTION from a repeating tile pattern?

This pattern type has these characteristics:
- The input is a large grid divided into uniform cells/tiles by a repeating grid line pattern (horizontal and vertical separator lines of a single color)
- The separator lines create a regular NxM grid of identical-sized cells
- Most cells contain only the background color (typically zeros) and the grid line color
- Some cells have a DIFFERENT color at the intersection points of the grid lines (marker colors)
- The output is a small grid where each cell represents one tile/intersection from the input
- The output captures which marker colors appear at each grid intersection, with background color for unmarked intersections

Look at the training examples:
- Is there a regular repeating grid pattern with uniform separator lines?
- Are there scattered "marker" colors that differ from both the background and grid line color?
- Is the output much smaller than the input (roughly the number of tiles)?
- Does the output seem to summarize which markers appear at which grid positions?

Answer ONLY with: YES or NO"""
