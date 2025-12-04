CLASSIFIER_PROMPT = """Does this puzzle exhibit SHADOW/TRAIL EXTENSION from colored blocks?

Look for these indicators:
- The input contains multiple small rectangular blocks (typically 2x2) of non-zero colored cells scattered on a background
- Each colored block has a specific position in the grid
- In the output, each colored block remains in place but gains an EXTENSION or "shadow" made of a single uniform color
- The extension fills the space between each block and the nearest grid edge (top, bottom, or sides)
- The shadow/trail color is consistent across all blocks (a single "fill" color used throughout)
- The extensions appear to project from each block toward the edges of the grid

Check if:
- Original colored blocks are preserved exactly
- A new uniform-colored region extends from each block toward grid boundaries
- The extension direction seems to go toward the nearest edge or continues until hitting another feature

Answer ONLY with: YES or NO"""
