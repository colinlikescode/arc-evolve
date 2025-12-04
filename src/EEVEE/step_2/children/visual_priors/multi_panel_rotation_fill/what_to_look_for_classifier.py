CLASSIFIER_PROMPT = """Does this puzzle involve MULTI-PANEL ROTATION/REFLECTION FILLING?

Look for these indicators:
- The input grid is divided into multiple equal-sized sections by separator columns (a single repeated value acting as a divider)
- The first section contains a colored pattern while other sections are empty (filled with zeros/background)
- The output keeps the separators and first section unchanged
- The empty sections are filled with rotated or reflected versions of the first section's pattern

Specifically check:
- Is there a vertical separator dividing the grid into panels?
- Is only the leftmost panel populated in the input?
- In the output, are the other panels filled with transformed versions of the first panel?

Answer ONLY with: YES or NO"""
