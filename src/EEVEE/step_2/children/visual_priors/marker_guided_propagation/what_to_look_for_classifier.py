CLASSIFIER_PROMPT = """Does this puzzle involve MARKER-GUIDED COLOR PROPAGATION?

Marker-guided propagation means:
- There is a distinct "marker" color scattered throughout the grid (often appearing as isolated cells or short lines)
- There are multiple colored shapes/regions in the input
- The marker cells indicate paths or directions along which colors should propagate/extend
- In the output, the marker cells are removed (or replaced)
- Colored regions extend along the paths where markers were located
- The output may be slightly smaller as marker columns/rows are consolidated

Look at the training examples:
- Is there a single color that appears as scattered single cells or short segments (acting as markers)?
- Do other colored shapes appear to extend or propagate in the output?
- Are the marker cells absent in the output, replaced by propagated colors?
- Does the output appear to be a "compressed" or "consolidated" version where markers guided movement?

Answer ONLY with: YES or NO"""
