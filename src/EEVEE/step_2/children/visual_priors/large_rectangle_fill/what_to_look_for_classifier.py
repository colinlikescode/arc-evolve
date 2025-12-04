CLASSIFIER_PROMPT = """Does this puzzle involve FINDING LARGE SOLID RECTANGLES and FILLING them with a new color?

Look for these indicators:

1. INPUT contains:
   - Multiple regions of different colors
   - Some regions form SOLID RECTANGLES (all cells same color, rectangular shape)
   - These rectangles are relatively LARGE (not just 1-2 cells)

2. OUTPUT shows:
   - Large solid rectangles have been RECOLORED to a specific color (like yellow/4)
   - Only the large rectangular regions changed
   - Smaller shapes or irregular shapes remain unchanged

3. Key characteristics:
   - A "solid rectangle" means ALL cells within the bounding box are the same color
   - There's a SIZE THRESHOLD - only rectangles above a certain size get filled
   - The fill color is consistent (same color for all detected rectangles)

What to look for:
- Are there uniform rectangular blocks in the input?
- Do those blocks change to a single new color in the output?
- Do smaller or irregular shapes stay the same?

Answer ONLY with: YES or NO"""

