CLASSIFIER_PROMPT = """Does this puzzle involve HOLLOWING OUT SOLID RECTANGLES?

Look for these indicators:
- The input contains multiple solid (filled) rectangular regions of non-background colors
- Each rectangle is a uniform block of a single color
- In the output, each rectangle's OUTER BORDER (1 cell thick) remains the original color
- The INTERIOR of each rectangle is filled with a different uniform color (the same fill color for all rectangles)
- The rectangles essentially become "frames" or "hollow boxes" with filled interiors

Check:
- Are there solid rectangular shapes in the input?
- Do those shapes become outlined/framed versions in the output?
- Is the interior replaced with a consistent new color across all shapes?

Answer ONLY with: YES or NO"""
