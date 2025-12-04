CLASSIFIER_PROMPT = """Does this puzzle exhibit TEMPLATE STAMPING AT MARKER POSITIONS?

Template stamping at marker positions means:
- The input contains a small colored pattern/template in one corner (typically separated by a divider line)
- The rest of the grid is mostly empty (background color) except for scattered single marker cells
- Each marker cell indicates a position where the template should be "stamped" or copied
- The template is placed such that the marker position aligns with a specific cell within the template (often the center or a consistent position)

Look at the training examples:
- Is there a distinct colored pattern in one section of the grid (often top-left)?
- Is there a vertical or horizontal divider line separating the template from the rest?
- Are there isolated single-cell markers scattered in the otherwise empty region?
- In the output, does the template appear copied at each marker location?
- Does the marker position correspond to a specific cell within each stamped template?

Answer ONLY with: YES or NO"""
