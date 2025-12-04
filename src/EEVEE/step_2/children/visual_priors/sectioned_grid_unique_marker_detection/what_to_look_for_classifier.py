CLASSIFIER_PROMPT = """Does this puzzle involve a GRID DIVIDED INTO SECTIONS with UNIQUE MARKER DETECTION?

Look for these indicators:
- The input grid is divided into a regular arrangement of sections by divider lines (rows/columns filled with a single separator color)
- Each section contains scattered marker cells on a background
- The output is a smaller grid where each cell corresponds to one section
- The output appears to indicate which sections have markers in positions that are UNIQUE (not shared with other sections)

Check:
- Are there horizontal and vertical divider lines creating a grid of regions?
- Does the output size match the number of regions (e.g., 3x3 regions → 3x3 output)?
- Do output values seem to flag sections with distinctive/unique marker placements?

Answer ONLY with: YES or NO"""
