CLASSIFIER_PROMPT = """Does this puzzle exhibit DIRECTIONAL MARKER EXTENSION/PROJECTION?

Directional marker extension means:
- The input grid has two main background colors plus a small cluster of a distinct "marker" color
- The marker color forms a small connected shape (line segment, small rectangle, or L-shape)
- The marker shape indicates a direction (horizontal, vertical, or diagonal based on its orientation)
- In the output, the marker pattern is extended/projected along that direction
- The extension replaces one of the background colors with the marker color

Look at the training examples:
- Is there a small cluster of a distinct color (not the two dominant background colors)?
- Does this cluster form a linear or directional shape?
- In the output, does this pattern extend in the direction it "points"?
- Does the extension only replace one specific background color (not the other)?

Answer ONLY with: YES or NO"""
