CLASSIFIER_PROMPT = """Does this puzzle involve EXTRACTING AND COMPLETING A GRID PATTERN FROM A NOISY RECTANGLE?

Look for these indicators:
- The input contains a large grid filled mostly with random/noisy values
- There is a rectangular region filled predominantly with ONE color (the "fill color")
- Within this filled rectangle, there are a few scattered cells of a DIFFERENT color (the "marker color")
- The output is a smaller grid showing a regular pattern made of just these two colors
- The marker cells within the filled region indicate where "lines" or divisions occur in the pattern
- The output reconstructs a complete regular grid pattern (like a lattice or mesh) based on the marker positions

The transformation:
1. Find the rectangular region dominated by one color
2. Identify the sparse marker cells of a different color within that region
3. The markers indicate row/column positions of grid lines
4. Output a complete pattern where marker rows/columns become full lines of the marker color, and the rest uses the fill color

Answer ONLY with: YES or NO"""
