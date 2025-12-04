CLASSIFIER_PROMPT = """Does this puzzle involve PROPAGATION FROM A SOURCE BLOCK with DIAGONAL and STAIRCASE patterns?

Look for these indicators:

1. INPUT contains:
   - A solid rectangular BLOCK of one color (like 8/blue) = the SOURCE
   - Some barrier cells (like 5) scattered around
   - Background is mostly 0s

2. OUTPUT shows PROPAGATION from the source block:
   - DIAGONAL lines extending from the CORNERS of the source block (one color, like red/2)
   - STAIRCASE or ZIGZAG patterns extending from the EDGES of the source block (another color, like yellow/4)
   - Propagation STOPS when hitting barrier cells (5s)

3. The staircase pattern alternates directions:
   - Goes OUT a few steps, then SIDEWAYS a few steps, repeating
   - Creates a stepped/zigzag appearance

Key signs:
- Solid rectangular source block in input
- New colors appear in output radiating FROM the source
- Corner diagonals and edge staircases visible
- Barriers (5s) block the propagation

Answer ONLY with: YES or NO"""

