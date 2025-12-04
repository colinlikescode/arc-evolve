CLASSIFIER_PROMPT = """Does this puzzle involve BOUNDED REGION EXTRACTION with TEMPLATE-BASED FILLING?

Look for these indicators:
- The input contains a rectangular region marked by CORNER MARKERS (same color at 4 corners forming a rectangle)
- Inside this bounded region, there are multiple colored BLOCKS/SHAPES (not the corner marker color)
- Somewhere OUTSIDE the bounded region, there is a small TEMPLATE PATTERN showing spatial relationships between colors
- The template uses single cells or small markers to indicate which colors should be adjacent/connected

The transformation:
- Extracts the bounded rectangular region (defined by corner markers)
- Uses the external template to determine how the colored blocks should EXPAND or CONNECT
- Fills gaps between blocks according to the template's spatial layout

Look at training examples:
- Are there 4 identical colored cells forming corners of a rectangle?
- Are there colored shapes inside this rectangle?
- Is there a separate small pattern outside showing color relationships?
- Does the output preserve the corner markers and original shapes but add filling between them?

Answer ONLY with: YES or NO"""
