CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE MATCHING WITH RECOLORING based on a reference region?

Look for these indicators:
- A grid divided into regions by a distinctive "divider" color forming lines (horizontal and vertical)
- One region (typically top-left) contains a "template" shape
- Other shapes scattered throughout the grid
- Some shapes have the SAME geometric form as the template (possibly rotated or reflected)
- In the output, shapes matching the template's form get recolored to the divider color

Key questions:
- Is there a divider pattern (cross, L-shape, or lines) made of a consistent color?
- Does one bounded region contain a reference/template shape?
- Do other shapes in the grid share the same geometric pattern as the template?
- Are matching shapes recolored while non-matching shapes stay the same?

Answer ONLY with: YES or NO"""
