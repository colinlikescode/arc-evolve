CLASSIFIER_PROMPT = """Does this puzzle involve INTERIOR HOLE FILLING?

Interior hole filling means:
- The grid contains a background value (typically zero) scattered throughout
- Some background cells are connected to the grid's outer boundary (edges)
- Other background cells are "trapped" in the interior, not connected to any edge
- The transformation fills the interior/trapped background cells with a different value
- Background cells connected to the boundary remain unchanged

Look at the training examples:
- Does the grid have scattered background (zero) cells?
- In the output, do some zeros remain while others are replaced?
- Do the zeros that remain appear to be connected to the grid edges?
- Do the zeros that get replaced appear to be "enclosed" by non-zero values?

Answer ONLY with: YES or NO"""
