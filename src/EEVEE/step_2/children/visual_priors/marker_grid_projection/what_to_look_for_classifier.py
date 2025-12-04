CLASSIFIER_PROMPT = """Does this puzzle involve MARKER-BASED GRID LINE PROJECTION?

Look for these indicators:
- A rectangular shape with nested layers: an outer frame color surrounding an inner filled region
- Single "marker" cells of the inner fill color that appear within the frame layer (protruding from the inner region)
- These markers appear on edges of the inner region, not as part of the main filled area
- The output shows grid lines drawn through the inner region at marker positions
- Lines extend beyond the shape's boundary into the background area

The pattern involves using isolated marker cells to define where to draw dividing lines that:
1. Subdivide the inner region (using the frame color)
2. Project outward into the background (using the inner fill color)

Answer ONLY with: YES or NO"""
