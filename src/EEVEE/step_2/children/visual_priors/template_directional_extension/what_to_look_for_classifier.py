CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE-BASED DIRECTIONAL EXTENSION/PROJECTION?

Look for these indicators:
- A small "template" pattern containing two distinct non-background colors: a primary shape color and a marker/anchor color
- The marker color appears at specific positions relative to the primary shape (indicating direction)
- Separate rectangular blocks of ONLY the marker color appear elsewhere in the grid
- In the output, each marker block has the primary shape pattern extended/projected from it
- The direction of extension is determined by the relative position of markers in the template
- The extension may be scaled based on the size of the marker block

Key questions:
- Is there a template with a shape and directional markers?
- Are there standalone marker-colored rectangles that act as "anchors"?
- Does the output show the shape pattern emanating from these anchor blocks?

Answer ONLY with: YES or NO"""
