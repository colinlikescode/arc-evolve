CLASSIFIER_PROMPT = """Does this puzzle involve CONNECTED COMPONENT COLORING BY SHAPE/ORIENTATION?

Look for these indicators:
- The input has scattered marker cells (one non-background color) on a uniform background
- The output replaces these marker cells with DIFFERENT colors based on their grouping
- Adjacent marker cells (sharing an edge) form connected components
- Each connected component is colored based on its SIZE or SHAPE/ORIENTATION:
  - Isolated single cells get one color
  - Horizontally adjacent pairs get a different color
  - Vertically adjacent pairs get another color
  - The background remains unchanged

Check the training examples:
- Are marker cells being recolored based on how they connect to neighbors?
- Do horizontal pairs get a consistent color across all examples?
- Do vertical pairs get a different consistent color?
- Do isolated cells get their own consistent color?

Answer ONLY with: YES or NO"""
