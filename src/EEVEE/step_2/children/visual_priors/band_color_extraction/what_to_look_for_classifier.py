CLASSIFIER_PROMPT = """Does this puzzle exhibit VERTICAL STRIPE/BAND COLOR EXTRACTION?

This pattern means:
- The input grid contains multiple distinct vertical bands/stripes of different colors
- The boundaries between bands are irregular/wavy (not perfectly straight vertical lines)
- Each band is dominated by a single color, though the edges may be noisy/imperfect
- The output extracts the unique colors from left to right (or top to bottom for horizontal bands)
- The output is a single row (for vertical bands) or single column (for horizontal bands) listing the band colors in spatial order

Look at the training examples:
- Does the input appear to have distinct colored regions arranged as vertical or horizontal stripes?
- Are there 2-4+ different dominant colors, each occupying a rough band/region?
- Is the output a 1×N or N×1 grid listing colors in the order they appear spatially?
- Do the band boundaries appear wavy/irregular rather than perfectly straight?

Answer ONLY with: YES or NO"""
