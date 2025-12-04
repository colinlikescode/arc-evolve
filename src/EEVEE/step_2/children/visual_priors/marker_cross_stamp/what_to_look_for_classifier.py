CLASSIFIER_PROMPT = """Does this puzzle exhibit a MARKER EXPANSION / STAMP PATTERN?

Marker expansion means:
- The input contains scattered single cells of a specific marker color on a background
- Each marker cell is replaced/expanded with a small fixed template pattern in the output
- The template is typically a cross/plus shape or small geometric pattern centered on the marker
- The same template is applied consistently to ALL marker positions
- Parts of the template may be clipped when near grid boundaries

Look at the training examples:
- Are there isolated single cells of one color scattered in the input?
- In the output, do these positions become centers of identical small patterns?
- Does the pattern around each marker look like a cross, plus, or small symmetric shape?
- Are multiple new colors introduced in the output that weren't in the input?

Answer ONLY with: YES or NO"""
