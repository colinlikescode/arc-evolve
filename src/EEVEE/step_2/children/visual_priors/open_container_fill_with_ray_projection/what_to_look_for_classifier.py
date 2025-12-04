CLASSIFIER_PROMPT = """Does this puzzle involve FILLING AN OPEN CONTAINER AND PROJECTING RAYS FROM ITS OPENING?

Look for these indicators:
- The input contains a shape made of non-zero cells that forms a partial enclosure (like a cup, bracket, or frame with a gap/opening)
- The shape has an interior region and an opening facing toward empty space
- In the output, the interior of the shape is filled with a new color
- Additionally, rays or lines extend outward from the opening into the previously empty region
- The rays project in the direction the opening faces (diagonally, horizontally, or vertically)

Key characteristics:
- The original shape cells remain unchanged
- A new fill color appears both inside the shape AND extending outward
- The extension follows the geometry of the opening (continuing the gap's trajectory)

Answer ONLY with: YES or NO"""
