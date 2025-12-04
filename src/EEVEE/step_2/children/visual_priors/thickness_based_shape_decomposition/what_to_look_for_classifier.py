CLASSIFIER_PROMPT = """Does this puzzle involve THICKNESS-BASED SHAPE DECOMPOSITION?

Thickness-based decomposition means:
- The input contains a connected shape made of a single non-zero color
- The output recolors cells based on whether they belong to "thick" regions (2x2 blocks) or "thin" regions
- Cells that are part of at least one 2x2 block of the shape get one color
- Cells that are NOT part of any 2x2 block get a different color
- The overall shape outline remains the same, only the coloring changes

Look at the training examples:
- Is there a single connected shape in the input using one non-zero color?
- In the output, are there exactly two different non-zero colors?
- Do the colors appear to distinguish between thick/solid regions and thin/line regions?
- Are 2x2 solid blocks colored differently from isolated cells or single-width lines?

Answer ONLY with: YES or NO"""
