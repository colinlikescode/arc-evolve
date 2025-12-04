CLASSIFIER_PROMPT = """Does this puzzle exhibit CROSS-DIVIDER QUADRANT TILING?

Cross-divider quadrant tiling means:
- The grid is divided into quadrants (or sections) by one or more lines of a single repeated color that span the entire width or height
- These divider lines form a cross pattern (horizontal and/or vertical lines)
- One quadrant contains a pattern with colored cells (the "source" quadrant)
- Other quadrants are mostly empty (filled with background color)
- The transformation copies/tiles the source pattern into all empty quadrants

Look at the training examples:
- Is there a horizontal and/or vertical line of a single color that divides the grid into sections?
- Does one section contain scattered colored cells while other sections are empty?
- Does the output show the same pattern replicated across all sections?
- Are the divider lines preserved in the output?

Answer ONLY with: YES or NO"""
