CLASSIFIER_PROMPT = """Does this puzzle involve TEMPLATE RECONSTRUCTION FROM SCATTERED MARKERS?

Look for these indicators:
- The input contains a complete connected shape (template) made of one dominant connector color with distinct marker colors at key positions (corners, endpoints, center)
- The input also contains isolated single-cell markers scattered elsewhere that match the marker colors from the template
- The output removes the original template shape
- The output reconstructs the template pattern at new locations where the scattered markers define the anchor points
- The connector color fills in the paths/lines between the relocated marker positions

Key pattern: A template shape defines a spatial relationship between marker colors, and that relationship is replicated wherever matching markers appear scattered in the grid.

Answer ONLY with: YES or NO"""
