CLASSIFIER_PROMPT = """Does this puzzle exhibit HORIZONTAL BAND DENOISING / STRIPE CLEANING?

This pattern means:
- The grid is divided into horizontal bands (stripes/rows of consistent color)
- Each band has a DOMINANT color that appears most frequently in that region
- Some cells within each band contain "noise" - scattered cells of different colors that don't belong
- The transformation removes the noise by replacing all cells in each band with that band's dominant color

Look at the training examples:
- Is the grid visually organized into horizontal stripes/bands?
- Does each band have one color that appears much more often than others?
- Are there sporadic "wrong" colored cells scattered within bands?
- Does the output show clean, uniform horizontal bands with no noise?
- Do the bands maintain their relative positions and approximate widths?

Answer ONLY with: YES or NO"""
